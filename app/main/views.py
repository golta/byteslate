from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import *
from ..models import *
from app.email import *

@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@main.route('/email')
def email():
	print "In main context"
	send_event_notification.delay('rahul.rrixe@gmail.com')
	return "hello txt"