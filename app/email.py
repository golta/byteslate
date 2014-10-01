from app import mail, db
from celery.signals import task_postrun
from flask.ext.mail import Message
from app import create_celery_app
#import requests

celery = create_celery_app()

def hello():
	print 'hello'

@celery.task
def send_event_notification(*recepients):
	'''
	msg = Message(
		'Your Next Event is On',
		sender='admin@bytecode.com',
		recipients=[user]
	)
	
	msg.body = render_template(
		'mail/notification.mail'
		user=user,
		token=token
	)
	
	mail.send(msg)
	'''
	print "sent the mail"

@task_postrun.connect
def close_session(*args, **kwargs):
	db.session.remove()