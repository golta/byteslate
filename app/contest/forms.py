from wtforms import *
from wtforms.validators import *
from flask.ext.wtf import Form

class ContestAddForm(Form):
	title = StringField('Title', validators=[Required(), Length(1,29)] )
	description = TextAreaField('Description', validators=[Required(), Length(1,159)] )
	start_time = DateTimeField('Start time', validators=[Required()] )
	end_time = DateTimeField('End time', validators=[] )
	url = StringField('Url', validators=[Required()] )
	arena = SelectField('Arena', coerce=int)
	submit = SubmitField('Save')