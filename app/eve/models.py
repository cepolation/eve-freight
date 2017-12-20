from flask_sqlalchemy import SQLAlchemy
from app import db

class ESIToken(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# CHARACTER
	character_id = db.Column(db.Integer)
	character_owner_hash = db.Column(db.String(256))
	character_name = db.Column(db.String(256))
	# SSO
	access_token = db.Column(db.String(256)) 
	refresh_token = db.Column(db.String(256)) 

class Contract(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	contract_id = db.Column(db.Integer)
	issuer_id = db.Column(db.Integer)
	issuer_corporation_id = db.Column(db.Integer)
	assignee_id = db.Column(db.Integer)
	acceptor_id = db.Column(db.Integer)
	contract_type = db.Column(db.String(256))
	contract_status = db.Column(db.String(256))
	contract_reward = db.Column(db.Integer)
	contract_volume = db.Column(db.Integer)
