from __future__ import unicode_literals
from haystack import indexes

from comms.models import SMS, Email, EmailTemplate, SmsTemplate


class SmsIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=False)
    to = indexes.CharField(model_attr="to")
    message = indexes.CharField(model_attr="message")
    sent_on = indexes.DateTimeField(model_attr="sent_on")

    def get_model(self):
        return SMS

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class EmailIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=False)
    to = indexes.CharField(model_attr="to")
    subject = indexes.CharField(model_attr="subject")
    message = indexes.CharField(model_attr="message")
    sent_on = indexes.DateTimeField(model_attr="sent_on")

    def get_model(self):
        return Email

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class EmailTemplateIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=False)
    subject = indexes.CharField(model_attr="subject")
    body = indexes.CharField(model_attr="body")
    type = indexes.CharField(model_attr="type")

    def get_model(self):
        return EmailTemplate

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class SmsTemplateIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=False)
    body = indexes.CharField(model_attr="body")
    type = indexes.CharField(model_attr="type")

    def get_model(self):
        return SmsTemplate

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
