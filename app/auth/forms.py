from wtforms import *
from wtforms.validators import *
from flask.ext.wtf import Form

class LoginForm(Form):
	username = StringField('Username', validators=[Required(), Length(1,30)] )
	password = PasswordField('Password', validators=[Required()] )
	submit = SubmitField('Log In')