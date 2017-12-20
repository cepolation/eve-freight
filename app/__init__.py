from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.admin.views import admin
from app.main.views import main

app = Flask(__name__)
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
## CONFIG
app.config['SQL_USER'] = "root"
app.config['SQL_PASSWORD'] = "password"
app.config['ESI_CLIENT_ID'] = "d9e042c7462046018b867637ba6fe1cd"
app.config['ESI_SECRET_KEY'] = "fEL01TRwKRZKGsW48bnpNm3TInKcK7o5hmjsW7vS"
app.config['ESI_SCOPES'] = "esi-contracts.read_corporation_contracts.v1"
app.config['ESI_CALLBACK_URL'] = "http://localhost:5000/esi/callback"

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://' + app.config['SQL_USER'] + ':' + app.config['SQL_PASSWORD'] + '@localhost/dev'
db = SQLAlchemy(app)
