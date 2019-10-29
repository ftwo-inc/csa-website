from __future__ import unicode_literals
from builtins import str
from postmarker.core import PostmarkClient
from comms.models import Email as EM
from csa.utils.secrets import get_secret
from comms import tasks
import logging
logger = logging.getLogger(__name__)


def check_secrets():
    '''
    Checks to ensure keys are defined in env
    and returns in dict.
    :return:
    '''
    keys = dict()
    keys['server_token'] = get_secret('postmark_server_token')

    if '' in [keys[x] for x in list(keys.keys())]:
        raise NotImplementedError('Postmark Keys not found')
    else:
        return keys


def get_client(server_token):
    return PostmarkClient(server_token=server_token)


def send_mail(subject, message, recipient_list, from_email, attachments=[]):
    try:
        tasks.send_mail_task(check_secrets()['server_token'], subject, message, attachments, recipient_list,
                                   from_email)
        logger.info("An email was scheduled to send. " + str(recipient_list))
    except Exception as e:
        logger.error("An error occurred when scheduling an email for send. " + str(e))

    em = EM.objects.create(
        to=recipient_list,
        subject=subject,
        message=message
    )
    return em
