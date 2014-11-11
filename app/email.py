#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.mail import Message
from mailsnake import MailSnake
from mailsnake.exceptions import *
from flask import render_template
import requests


'''
FROM_EMAIL = 'subscribe@byteslate.com'
FROM_NAME  = u'Site Admin'
EMAIL_ARCHIVE = 'byteslate@byteslate.com'
MAILCHIMP_API_KEY = '892dd6868986917dae3ddb10d381b569-us9'
MANDRILL_API_KEY = 'Kk-su18k1OjqzCFUwMY6VQ'
mailchimp_api = MailSnake('MAILCHIMP_API_KEY')
'''
# using Mailgun for messaging
MAILGUN_API_KEY = "key-97a2dc8797b621297b67f72308ebfaaa"
MAILGUN_BASE_URL = "https://api.mailgun.net/v2/sandbox2718e14be9ab467d9ef07551dee1f399.mailgun.org/"



def send_email(to, subject, template, **kwargs):
	msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
	sender = app.config['FLASKY_MAIL_SENDER'], recipients=[to])
	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)
	mail.send(msg)


def mail_send(recipient, template, **kwargs):

    if template == 'welcome':
        send_welcome(recipient)
    elif template == 'confirmation_instructions':
        send_confirmation_instructions(recipient, **kwargs)
    elif template == 'login_instructions':
        send_login_instructions(**kwargs)
    elif template == 'reset_instructions':
        send_reset_instructions(**kwargs)
    elif template == 'reset_notice':
        send_reset_notice(**kwargs)
    else:
        return NotImplemented

# check whether it is correct email address
def get_validate(email):
    return requests.get(
        MAILGUN_BASE_URL+"validate",
        auth=("api", MAILGUN_API_KEY),
        params={"address": email})


def send_welcome(recipient):
    # get html object
    html = render_template('')

    try:
      return requests.post(
          MAILGUN_BASE_URL+"messages",
          auth=("api", MAILGUN_API_KEY),
          #files=[("attachment", open("files/test.jpg")),
          #       ("attachment", open("files/test.txt"))],
          data={"from": "no-reply@byteslate.com",
                "to": str(recipient),
                "bcc": "byteslate@byteslate.com",
                "subject": "Hello from ByteSlate",
                "text": "Testing some Mailgun awesomness!",
                "html": "<html>Welcome to the ByteSlate Club</html>"})
    except:
      print "Message sending failed :("

def send_confirmation_instructions(recipient, **data):
    # get html object
    html = render_template('email/action.html')
    print recipient
    try:
      return requests.post(
          MAILGUN_BASE_URL+"messages",
          auth=("api", MAILGUN_API_KEY),
          #files=[("attachment", open("files/test.jpg")),
          #       ("attachment", open("files/test.txt"))],
          data={"from": "no-reply@byteslate.com",
                "to": recipient,
                "subject": "Confirm your email address",
                "text": "Welcome to Byteslate Club",
                "html": html})
    except:
      print "Message sending failed :("

def send_login_instructions(**context):
    pass

def send_reset_instructions(**context):
    pass

def send_reset_notice(**context):
    pass

