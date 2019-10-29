from __future__ import unicode_literals
from comms import postmark as PM
from comms.twillio import send_message as SM
import traceback
from csa.utils.secrets import get_secret
import logging


def send_sms(to, body):
    return SM(to, body)


def send_sms_template(to, template=None, template_body=None, **kwargs):
    '''

    Function can either accept an SmsTemplate object, or a string.

    :param to:
    :param template:
    :param template_body:
    :param kwargs:
    :return:
    '''
    try:
        if template is not None:
            message = template.body
        else:
            message = template_body
        for key in list(kwargs.keys()):
            message = message.replace("*|" + key + "|*", kwargs.get(key))
        send_sms(to, message)
        return True
    except Exception as e:
        logging.error(e)
        return False


def send_email(subject, message, recipients, attachment, from_email):

    try:
        PM.send_mail(
            subject=subject,
            message=message,
            recipient_list=recipients,
            attachments=attachment,
            from_email=from_email
        )
        return True
    except Exception as e:
        logging.error(e)
        return False


def send_email_template(to, template=None, subject=None, template_body=None, from_email=None, **kwargs):
    '''

      Function can either accept an EmailTemplate object, or a string.

      :param to:
      :param template:
      :param template_body:
      :param kwargs:
      :return:
      '''
    try:
        if template_body is not None:
            message = template_body
        else:
            message = template.body

        if subject is None:
            subject = template.subject

        for key in list(kwargs.keys()):
            message = message.replace("*|"+key+"|*", kwargs[key])

        for key in list(kwargs.keys()):
            subject = subject.replace("*|"+key+"|*", kwargs[key])

        template_subject = subject if subject is not None else template.subject

        if from_email is None:
            from_email = get_secret('postmark_from_email')

        send_email(
            template_subject,
            message,
            [to],
            [],
            from_email
        )
        return True
    except Exception as e:
        logging.error(e)
        return False
