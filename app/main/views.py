from datetime import datetime
from flask import render_template, session, redirect, url_for, request, flash
from . import main
from .forms import SubscriptionForm
from ..models import *
#from ..email import send_mail

@main.route('/', methods=['GET', 'POST'])
def index():
	form = SubscriptionForm()
	if form.validate_on_submit():
		subscriber = Subscriber(email=form.email.data)
		db.session.add(subscriber)
		db.session.commit()
		#send_mail(subscriber.email, 'Confirm account', 'auth/email/confirm')  SEND MAIL HERE
		flash('Subscription received. A confirmation mail has been sent')
		return redirect(url_for('main.index'))
	return render_template('index.html', form=form)

@main.route('/confirm/<token>')
def confirm(token):
	subscriber = Subscriber.query.filter_by(secret_hash=token).first()
	if subscriber:
		subscriber.isactive = 1
		db.session.commit()
		flash('Subscription confirmed')
	else:
		flash('Invalid or expired request')
	return redirect(url_for('main.index') )

@main.route('/about', methods=['GET', 'POST'])
def about():
	return render_template('about.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
	return render_template('contact.html')

@main.route('/contest/<id>')
def contest_inner(id):
	# @TODO
	# fetch all the details of the contest using <id> and pass them as parameter below
	return render_template('contest/inner.html', id=id)