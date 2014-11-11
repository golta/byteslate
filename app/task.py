from app import mail, db
from celery.signals import task_postrun
import requests
from flask.ext.mail import Message
from app import create_celery_app
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from datetime import datetime
from utils import timeago
from models import Subscriber, Contest
from email import mail_send


celery = create_celery_app()
logger = get_task_logger(__name__)

#mailgun_api = "https://api.mailgun.net/v2/sandbox4255e3b61fd34434b1f7776d07147fb3.mailgun.org/messages"

@celery.task
def send_event_notification(*recepients):
	logger.info("Start task")
	msg = Message(
		'Your Next Event is On',
		sender='admin@bytecode.com',
		#recipients=[user]
	)

	msg.body = render_template(
		'mail/notification.mail'
		#user=user,
		#token=token
	)
	mail.send(msg)
	logger.info("Task finished: result")

@periodic_task(run_every=(crontab(hour="*", minute="*")))
def send_mail():

    logger.info("Start task")
    # get list of all contest which have time in next 24 hours
    contest_list = Contest.query.filter_by(event_time > datetime.now()).all()

    for contest in contest_list:
		diff_hour = (datetime.now() - contest.event_time).hours

		# send mail contest going to happen in next 24 hours
		if (diff_hour > 23 and diff_hour <= 24):
			subscriber_list = Subscriber.query.filter_by(isactive = 1).all()

			for subscriber in subscriber_list:
				mail_send(subscriber.email, 'Contest Notification', 'welcome')

    logger.info("Task finished: result")

@task_postrun.connect
def close_session(*args, **kwargs):
	db.session.remove()

