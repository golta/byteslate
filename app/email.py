#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.mail import Message
from mailsnake import MailSnake
from mailsnake.exceptions import *

FROM_EMAIL = 'subscribe@byteslate.com'
FROM_NAME  = u'Site Admin'
EMAIL_ARCHIVE = 'byteslate@byteslate.com'
MAILCHIMP_API_KEY = '892dd6868986917dae3ddb10d381b569-us9'
MANDRILL_API_KEY = 'Kk-su18k1OjqzCFUwMY6VQ'

mandrill_api = MailSnake('MANDRILL_API_KEY', api='mandrill')


def send_email(to, subject, template, **kwargs):
	msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
	sender = app.config['FLASKY_MAIL_SENDER'], recipients=[to])
	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)
	mail.send(msg)


def mail_send(subject, recipient, template, **kwargs):

    if template == 'welcome':
        send_welcome(**kwargs)
    elif template == 'confirmation_instructions':
        send_confirmation_instructions(**kwargs)
    elif template == 'login_instructions':
        send_login_instructions(**kwargs)
    elif template == 'reset_instructions':
        send_reset_instructions(**kwargs)
    elif template == 'reset_notice':
        send_reset_notice(**kwargs)
    else:
        return NotImplemented


def send_welcome(**kwargs):
    context = {}
    context['template_name'] = 'welcome'
    context['template_content'] = []
    context['message'] = {"subject": u"ByteSlate - Confirm Subscription :)",
                          "from_email": FROM_EMAIL,
                          "from_name":  FROM_NAME,
                          "to":[{"email": kwargs['user'].email}],
                          "track_opens":True,
                          "track_clicks":True,
                          "auto_text":True,
                          "url_strip_qs":False,
                          "preserve_recipients":False,
                          "bcc_address": EMAIL_ARCHIVE,
                          "merge_vars":[
                              {
                                  "rcpt": kwargs['user'].email,
                                  "vars":[{"name": "CONFIRMATION_LINK", "content": kwargs['confirmation_link']}]}],

                          "tags":["welcome"],

                          "recipient_metadata": [{
                              "rcpt": kwargs['user'].email,
                              "values": [{ "user_id": kwargs['user'].id}]}]
                         }
    try:
    	mandrill_api.messages.send_template(**context)
    except MailSnakeException:
    	print 'An error occurred. :('

def send_confirmation_instructions(**context):
    pass

def send_login_instructions(**context):
    pass

def send_reset_instructions(**context):
    pass

def send_reset_notice(**context):
    pass

