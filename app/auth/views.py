from flask import render_template, session, redirect, url_for, request, flash
from . import auth
from flask.ext.login import login_user
from ..models import Admin
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'] )
def login():
	form = LoginForm()
	if form.validate_on_submit():
		admin = Admin.query.filter_by(username=form.username.data, password=form.password.data).first()
		if admin is not None:
			login_user(admin)
			return redirect(url_for('main.index') )
		flash('Invalid username or password')
	return render_template('auth/login.html', form=form)