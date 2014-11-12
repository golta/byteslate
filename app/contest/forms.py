from wtforms import *
from wtforms.validators import *
from flask.ext.wtf import Form

class ContestAddForm(Form):
	title = StringField('Title', validators=[Required(), Length(1,29)] )
	description = TextAreaField('Description', validators=[Required(), Length(1,159)] )
	content = TextAreaField('Content', validators=[Required() ] )
	start_time = DateTimeField('Start time', validators=[Required()] )
	end_time = DateTimeField('End time', validators=[Required()] )
	url = StringField('Url', validators=[Required()] )
	arena = SelectField('Arena', coerce=int)
	prizes = RadioField('Prizes', choices=[ ('1', 'Yes'), ('0', 'No') ])
	hiring = RadioField('Hiring Event', choices=[ ('1', 'Yes'), ('0', 'No') ])
	submit = SubmitField('Save')

class ArenaAddForm(Form):
	title = StringField('Title', validators=[Required(), Length(1,29)] )
	submit = SubmitField('Save')
