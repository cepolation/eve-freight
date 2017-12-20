from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.admin.views import admin
from app.main.views import main

app = Flask(__name__)
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:password@localhost/dev'
app.config['ADMIN_KEY'] = '123'
db = SQLAlchemy(app)
