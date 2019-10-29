from __future__ import unicode_literals
from builtins import object
from rest_framework import serializers
from comms.models import Email, SMS


class EmailSerializer(serializers.Serializer):
    '''
    Send Email Serializer.
    '''

    subject = serializers.CharField(max_length=220)
    body = serializers.CharField(max_length=220)
    username_or_email = serializers.CharField(max_length=220, required=False)


class SmsSerializer(serializers.Serializer):
    '''
    Send SMS Serializer.
    '''

    body = serializers.CharField(max_length=100)


class ListEmailSerializer(serializers.ModelSerializer):
    '''
    List Email Serializer. User sends username_or_email field to get all Emails related to user.
    '''
    class Meta(object):
        model = Email
        fields = "__all__"


class RetrieveEmailSerializer(serializers.Serializer):
    '''
    Retrieve Email Serializer.
    '''

    id = serializers.IntegerField()
    to = serializers.CharField()
    message = serializers.CharField()


class EmailModelSerializer(serializers.ModelSerializer):
    '''
    Email logs Serializer.
    '''

    class Meta(object):

        from comms.models import Email  # Lazy Import

        model = Email
        fields = ['to', 'message']


class ListSmsSerializer(serializers.ModelSerializer):
    """
    List Sms Serializer.
    """
    class Meta(object):
        model = SMS
        fields = "__all__"


class RetrieveSmsSerializer(serializers.Serializer):
    '''
    Retrieve SMS Serializer.
    '''

    id = serializers.IntegerField()
    to = serializers.CharField()
    message = serializers.CharField()


class SmsModelSerializer(serializers.ModelSerializer):
    '''
    SMS logs Serializer.
    '''

    class Meta(object):

        from comms.models import SMS  # Lazy Import

        model = SMS
        fields = ['to', 'message']


class EmailTemplateSerializer(serializers.ModelSerializer):
    '''
    Email Template Serializer, used for Email Template: List, Create, Retrieve, Update, Delete.
    '''

    class Meta(object):

        from comms.models import EmailTemplate  # Lazy Import

        model = EmailTemplate
        fields = "__all__"


class SMSTemplateSerializer(serializers.ModelSerializer):
    '''
    SMS Template Serializer, used for SMS Template: List, Create, Retrieve, Update, Delete.
    '''

    class Meta(object):

        from comms.models import SmsTemplate  # Lazy Import

        model = SmsTemplate
        fields = "__all__"
