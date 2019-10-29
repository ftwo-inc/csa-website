from __future__ import unicode_literals
from builtins import object
from comms import models
from import_export import resources


class SmsResource(resources.ModelResource):
    class Meta(object):
        model = models.SMS
        exclude = ()


class EmailResource(resources.ModelResource):
    class Meta(object):
        model = models.Email
        exclude = ()


class EmailTemplateResource(resources.ModelResource):
    class Meta(object):
        model = models.EmailTemplate
        exclude = ()


class SmsTemplateResource(resources.ModelResource):
    class Meta(object):
        model = models.SmsTemplate
        exclude = ()
