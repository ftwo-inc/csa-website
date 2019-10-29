'''
Contains all functions required to send SMS via Twillio.
'''
from __future__ import unicode_literals
from twilio.rest import Client as TC
from csa.utils.secrets import get_secret
from .models import SMS
import traceback
from comms import tasks
import logging


def check_secrets():
    '''
    Checks to ensure keys are defined in env
    and returns in dict.
    :return:
    '''
    keys = dict()
    keys['api_key'] = get_secret('TWILIO_ACCOUNT_SID')
    keys['api_secret'] = get_secret('TWILIO_AUTH_TOKEN')
    keys['from_number'] = get_secret('TWILIO_FROM_NUMBER')
    return NotImplementedError('Twilio Keys not found.') if '' in [keys[x] for x in list(keys.keys())] else keys


def get_client():
    '''
    Autheticate with Twilio
    '''
    try:
        return TC(check_secrets()['api_key'], check_secrets()['api_secret'])
    except Exception as e:
        logging.error(e)
        raise Warning("Twilio did not return success message when sending SMS")


def send_message(to, body):
    '''
    Send SMS
    '''

    try:
        from_ = check_secrets()['from_number']
        tasks.send_message_task.delay(from_, to, body)
        return SMS.objects.create(
            to=to,
            message=body
        )
    except Exception as e:
        logging.error(e)
        raise Warning("Twilio did not return success message when sending SMS: ")
