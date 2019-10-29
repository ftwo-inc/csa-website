from __future__ import unicode_literals
from builtins import str
from celery.decorators import task
from postmarker.core import PostmarkClient
from csa.utils.secrets import get_secret
import logging
logger = logging.getLogger(__name__)


@task()
def send_mail_task(token, subject, message, attachments, recipient_list, from_email):
    logger.info("Sending scheduled Email")
    client = PostmarkClient(server_token=token)
    logger.info("Authenticated with Postmark")
    if not from_email or from_email in ['None', 'none', 'null', '']:
        from_email = get_secret("postmark_from_email")

    try:
        client.emails.send(
            From=from_email,
            To=recipient_list,
            Subject=subject,
            HtmlBody=message,
            Cc=get_secret("postmark_cc_email") if get_secret("postmark_cc_email") else None,
            Bcc=get_secret("postmark_bcc_email") if get_secret("postmark_bcc_email") else None,
        )
    except Exception as e:
        logger.error("Error when sending Postmark email.")
        logger.error(e)


@task()
def send_message_task(from_, to, body):
    logger.debug("Sending scheduled SMS")
    try:
        from comms.twillio import get_client
        client = get_client()
        client.messages.create(
            to=to,
            from_=from_,
            body=body
        )
    except Exception as e:
        logger.error("An error occurred when sending a scheduled SMS. ", str(to), str(e))


@task()
def msg91_send_otp(url, payload, headers):
    import http.client, json
    conn = http.client.HTTPConnection("api.msg91.com")
    conn.request(
        "POST",
        url,
        json.dumps(payload),
        headers
    )

    res = conn.getresponse()
    data = res.read()
    logger.debug(data)


@task
def msg91_send_sms(url, payload, headers):
    import http.client, json
    conn = http.client.HTTPConnection("api.msg91.com")
    conn.request(
        "POST",
        url,
        json.dumps(payload),
        headers
    )

    res = conn.getresponse()
    data = res.read()
    logger.debug(data)


@task
def send_scheduled_notification(notification=None):

    if notification is None:
        logger.debug("Must pass notification id.")
        return

    from comms.models import Notification
    notification = Notification.objects.filter(id=notification).first()

    if notification is None:
        logger.debug("You tried to send a scheduled notification with an object id that does not exist.")
        return

    notification.send()

