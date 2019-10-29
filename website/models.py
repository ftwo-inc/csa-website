from __future__ import unicode_literals

from django.db import models

import logging
logging.getLogger(__name__)


class JobPosting(models.Model):
    logo = models.FileField()
    link = models.CharField(max_length=220)
    title = models.CharField(max_length=220)
    location = models.CharField(max_length=220)
    description = models.CharField(max_length=220)


class Testimonials(models.Model):
    pic = models.FileField()
    content = models.CharField(max_length=440)
    name = models.CharField(max_length=220)
    company = models.CharField(max_length=220)
    logo = models.FileField()


class Franchise(models.Model):
    fullname = models.CharField(max_length=220)
    email = models.EmailField(max_length=220)
    mobile = models.CharField(max_length=220)
    location = models.CharField(max_length=220)
    comment = models.CharField(max_length=440)

    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def send_notifications(self, type=None):
        from comms.models import EmailTemplate, SmsTemplate
        if type is None:
            return
        elif type == "franchise-submit-to-customer":

            email_template = EmailTemplate.objects.filter(
                slug="to:customer|product:franchise|slug:submit-franchise-to-customer").first()
            # sms_template = SmsTemplate.objects.filter(
            #     slug="to:customer|product:franchise|slug:submit-franchise-to-customer").first()

            template_keys = {
                "email": self.email,
                "mobile": self.mobile,
                "created_on": str(self.created_on),
                "fullname": self.fullname
            }
            # Send email
            from comms.communication import send_email_template
            try:
                send_email_template(self.email, template=email_template, **template_keys)
                # send_sms_template('+91' + self.mobile, template=sms_template, **template_keys)
            except Exception as e:
                logging.error("An error occurred while submitting franchise to customer.")

        elif type == "franchise-submit-to-admin":

            email_template = EmailTemplate.objects.filter(
                slug="to:admin|product:franchise|slug:submit-franchise-to-admin").first()
            # sms_template = SmsTemplate.objects.filter(
            #     slug="to:customer|product:franchise|slug:submit-franchise-to-admin").first()

            template_keys = {
                "email": 'pawan@sqre1.com',
                "mobile": '8802900919',
                "created_on": str(self.created_on),
                "fullname": 'Pawan Katiyar'
            }
            # Send email
            from comms.communication import send_email_template
            try:
                send_email_template(self.email, template=email_template, **template_keys)
                # send_sms_template('+91' + self.mobile, template=sms_template, **template_keys)
            except Exception as e:
                logging.error("An error occurred while submitting franchise to admin.")
        else:
            return None


class Enroll(models.Model):
    fullname = models.CharField(max_length=220)
    email = models.EmailField(max_length=220)
    mobile = models.CharField(max_length=220)
    location = models.CharField(max_length=220)
    comment = models.CharField(max_length=440)

    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def send_notifications(self, type=None):
        from comms.models import EmailTemplate, SmsTemplate
        if type is None:
            return
        elif type == "enroll-submit-to-customer":

            email_template = EmailTemplate.objects.filter(
                slug="to:customer|product:enroll|slug:submit-enroll-to-customer").first()
            # sms_template = SmsTemplate.objects.filter(
            #     slug="to:customer|product:enroll|slug:submit-enroll-to-customer").first()

            template_keys = {
                "email": self.email,
                "mobile": self.mobile,
                "created_on": str(self.created_on),
                "fullname": self.fullname
            }
            # Send email
            from comms.communication import send_email_template
            try:
                send_email_template(self.email, template=email_template, **template_keys)
                # send_sms_template('+91' + self.mobile, template=sms_template, **template_keys)
            except Exception as e:
                logging.error("An error occurred while submitting enroll to customer.")

        elif type == "enroll-submit-to-admin":

            email_template = EmailTemplate.objects.filter(
                slug="to:admin|product:enroll|slug:submit-enroll-to-admin").first()
            # sms_template = SmsTemplate.objects.filter(
            #     slug="to:customer|product:enroll|slug:submit-enroll-to-admin").first()

            template_keys = {
                "email": 'pawan@sqre1.com',
                "mobile": '8802900919',
                "created_on": str(self.created_on),
                "fullname": 'Pawan Katiyar'
            }
            # Send email
            from comms.communication import send_email_template
            try:
                send_email_template(self.email, template=email_template, **template_keys)
                # send_sms_template('+91' + self.mobile, template=sms_template, **template_keys)
            except Exception as e:
                logging.error("An error occurred while submitting enroll to admin.")
        else:
            return None


class NewsAndUpdates(models.Model):
    image = models.ImageField()
    content = models.CharField(max_length=220)
    link = models.CharField(max_length=220)
