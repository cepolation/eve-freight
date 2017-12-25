from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.main.views import main
from app.eve.views import *

app = Flask(__name__)
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(eve, url_prefix='/eve')
## CONFIG
app.config['SQL_USER'] = "root"
app.config['SQL_PASSWORD'] = "password"
app.config['ESI_CLIENT_ID'] = "d9e042c7462046018b867637ba6fe1cd"
app.config['ESI_SECRET_KEY'] = "fEL01TRwKRZKGsW48bnpNm3TInKcK7o5hmjsW7vS"
app.config['ESI_CALLBACK_URL'] = "http://127.0.0.1:5000/eve/callback"

## ESI
from esipy import App as esiapp
from esipy import EsiClient, EsiSecurity
esi_app = esiapp.create(url="https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility")
esi_client = EsiClient(
        retry_requests=True,
        header={'User-Agent': 'Something CCP can use to contact you and that define your app'},
        raw_body_only=False,
        )
esi_security = EsiSecurity(
        app=esi_app,
        redirect_uri=app.config['ESI_CALLBACK_URL'],
        client_id=app.config['ESI_CLIENT_ID'],
        secret_key=app.config['ESI_SECRET_KEY'],
        )
client=EsiClient(security=esi_security)
app.config['ESI_REDIRECT_URL'] = esi_security.get_auth_uri(
        scopes=['esi-contracts.read_corporation_contracts.v1'],
        state="None"
        )
app.config['esi_security'] = esi_security
app.config['esi_client'] = esi_client

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://' + app.config['SQL_USER'] + ':' + app.config['SQL_PASSWORD'] + '@localhost/dev'
db = SQLAlchemy(app)
