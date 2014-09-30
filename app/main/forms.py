from wtforms import *
from wtforms.validators import *
from flask.ext.wtf import Form

class SubscriptionForm(Form):
	email = StringField('Email', validators=[Required(), Length(1,50), Email()] )
	submit = SubmitField('Subscribe')