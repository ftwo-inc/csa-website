from __future__ import unicode_literals
from builtins import str
from django.db import models
from django.contrib.postgres.fields import JSONField


class SMS(models.Model):
    '''
    Logs all out bound SMS.
    '''
    to = models.TextField()
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)

    def get_customer_sms(user):
        return SMS.objects.filter(to=user.customer.country_code + user.customer.mobile)

    def __str__(self):
        return self.to


class Email(models.Model):
    '''
    Records a log of all out bound Email.
    '''

    to = models.TextField()
    subject = models.TextField()
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)

    def get_customer_mails(user):
        return Email.objects.filter(to=user.customer.email)

    def __str__(self):
        return self.to


class Notification(models.Model):
    '''
    Records a log of all out bound Notifications
    '''

    channel = models.TextField()
    event = models.TextField()
    data = JSONField()
    extra_data = JSONField()
    created_on = models.DateTimeField(auto_now_add=True)
    expo = models.BooleanField()

    scheduled = models.BooleanField(default=False)

    cron_minute = models.TextField()
    cron_hour = models.TextField()
    cron_day_of_week = models.TextField()
    cron_day_of_month = models.TextField()
    cron_month = models.TextField()

    periodic_task_id = models.IntegerField(null=True, blank=True)

    last_sent_on = models.DateTimeField(null=True, blank=True)

    def schedule(self):
        from djcelery.models import CrontabSchedule, PeriodicTask
        import json
        schedule = CrontabSchedule.objects.create(
            minute=self.cron_minute,
            hour=self.cron_hour,
            day_of_week=self.cron_day_of_week,
            day_of_month=self.cron_day_of_month,
            month_of_year=self.cron_month,
        )

        pc = PeriodicTask.objects.create(
            crontab=schedule,
            name='Periodic Notifications ID ' + str(self.id),
            task='comms.tasks.send_scheduled_notification',
            kwargs=json.dumps({"notification": self.id}),
        )

        pc.enabled = True
        pc.save()

        self.periodic_task_id = pc.id
        return self.save()

    @property
    def periodic_task(self):
        from djcelery.models import PeriodicTask
        return PeriodicTask.objects.filter(id=self.periodic_task_id).first()

    def deschedule(self):
        periodic_task = self.periodic_task
        self.periodic_task_id = None
        self.scheduled = False
        self.save()
        periodic_task.delete()
        return self

    def send(self):
        from comms.push.push import push
        import datetime

        push(self.channel, {'title': self.title, 'body': self.body, 'extra_data': self.extra_data},
             event=self.event, expo=True)

        self.last_sent_on = datetime.datetime.now()
        return self.save()

    @property
    def title(self):
        try:
            return self.data['title']
        except Exception as e:
            return "error: " + str(e)

    @property
    def body(self):
        try:
            return self.data['body']
        except Exception as e:
            return "error: " + str(e)

    @property
    def crontab(self):
        return " ".join([self.cron_minute, self.cron_hour, self.cron_day_of_week, self.cron_day_of_month,
                         self.cron_month])


class EmailTemplate(models.Model):
    '''
    Email Tempalates
    '''

    subject = models.TextField()
    body = models.TextField()
    slug = models.CharField(max_length=100, null=True, blank=True)


class SmsTemplate(models.Model):
    '''
    SMS Templates
    '''

    body = models.TextField()
    slug = models.CharField(max_length=100, null=True, blank=True)
