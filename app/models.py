from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
from app import db
import time
import hashlib
from flask.ext.login import UserMixin
from . import login_manager

salt = "uhfejs@"

@login_manager.user_loader
def load_user(user_id):
	return Admin.query.get(int(user_id))

class Base(db.Model):
	__abstract__ = True
	
	id = db.Column(db.Integer, primary_key=True)
	isactive = db.Column(db.Boolean(), default=0, nullable=False)
	isdeleted = db.Column(db.Boolean(), default=0, nullable=False)
	added_on = db.Column(db.DateTime(), default=db.func.current_timestamp(), nullable=False)
	modified_on = db.Column(db.DateTime(), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

class Subscriber(Base):
	__tablename__ = 'subscribers'

	email = db.Column(db.String(64), unique=True, index=True, nullable=False)
	secret_hash = db.Column(db.String(128), nullable=False)
		
	def __repr__(self):
		return '<User: %r>' % self.email

	def __init__(self, email):
		self.email = email
		input_secret = salt + repr(time.time())
		self.secret_hash = self.generate_secret(input_secret)

	def generate_secret(self, input_secret):
		return hashlib.md5(input_secret).hexdigest()

	def verify_secret(self, input_secret):
		return check_password_hash(self.secret_hash, input_secret)

class Contest(Base):
	__tablename__ = 'contests'

	title = db.Column(db.String(30), nullable=False)
	description = db.Column(db.String(160), nullable=False)
	start_time = db.Column(db.DateTime(), nullable=False)
	end_time = db.Column(db.DateTime(), nullable=False)
	url = db.Column(db.String(200), nullable=False)
	arena_id = db.Column(db.Integer, db.ForeignKey('arena.id'), nullable=False)
	
	def __repr__(self):
		return '<Contest: %r>' % self.title

	def __init__(self, title):
		self.title = title


class Admin(Base, UserMixin):
	__tablename__ = 'admin'

	username = db.Column(db.String(30), nullable=False)
	password = db.Column(db.String(30), nullable=False)

	def __repr__(self):
		return '<Admin: %r>' % self.username

class Arena(Base):
	__tablename__ = 'arena'

	title = db.Column(db.String(20), nullable=False)

	def __repr__(self):
		return '<Arena: %r>' % self.title

	def __init__(self, title):
		self.title = title;
