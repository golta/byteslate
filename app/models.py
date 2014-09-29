from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
from app import db
import time
import hashlib

salt = "uhfejs@"

class Subscriber(db.Model):
	__tablename__ = 'subscribers'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index=True)
	secret_hash = db.Column(db.String(128))
	isactive = db.Column(db.Boolean(), default=False)
	isdeleted = db.Column(db.Boolean(), default=False)
	added_on = db.Column(db.DateTime())

	def __repr__(self):
		return '<User: %r>' % self.email

	def __init__(self):
		input_secret = salt + repr(time.time())
		self.secret_hash = self.generate_secret(input_secret)

	def generate_secret(self, input_secret):
		return hashlib.md5(input_secret).hexdigest()

	def verify_secret(self, input_secret):
		return check_password_hash(self.secret_hash, input_secret)

class Contest(db.Model):
	__tablename__ = 'contests'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(30))
	description = db.Column(db.String(160))
	event_time = db.Column(db.DateTime())
	duration = db.Column(db.Interval())
	arena = db.Column(db.String(40))
	url = db.Column(db.String(200))
	added_on = db.Column(db.DateTime())
	isactive = db.Column(db.Boolean(), default=False)
	isdeleted = db.Column(db.Boolean(), default=False)

	def __repr__(self):
		return '<Contest: %r>' % self.title

	def __init__(self):
		self.added_on = int(time.time())
