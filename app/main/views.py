from datetime import datetime
from flask import render_template, session, redirect, url_for, request, flash
from . import main
from .forms import SubscriptionForm
from ..models import *
from app.email import *


@main.route('/email')
def email():
	print "In main context"
	send_event_notification.delay('rahul.rrixe@gmail.com')
	return "hello txt"

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
	contests = Contest.query.all()
	return render_template('index.html', form=form, contests=contests)

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

@main.route('/contest/<title>/<id>')
def contest_inner(title, id):
	# @TODO
	# fetch all the details of the contest using <id> and pass them as parameter below
	contest = Contest.query.filter_by(id=id).first()
	print contest
	return render_template('contest/inner.html', contest=contest)
