from __future__ import unicode_literals
from builtins import str
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions
from comms.models import SMS, Email, SmsTemplate, EmailTemplate
from user.utils import common
from user.utils import get
from comms import serializers, communication
from customer.models import Customer
from comms import models
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import TemplateView


class SendEmail(GenericAPIView):
    '''
    A generic API that allows you to send Email
    to the logged in user or a different one.
    '''

    permission_classes = (IsAuthenticated,)
    serializer_classes = serializers.EmailSerializer

    def post(self, request, *args, **kwargs):

        if 'username_or_email' in list(request.data.keys()):
            if request.data.get('username_or_email') is not None:
                user = get.get_user(request.data.get('username_or_email'))
        else:
            user = request.user
        subject = self.request.data.get("subject")
        message = self.request.data.get("message")

        if user is not None and user.customer.has_email():
            if communication.send_email(subject, message, user.customer.email, []):
                return Response({'message': 'Email sent'}, status=status.HTTP_200_OK)

        return Response({'message': 'Email could not be sent.'
                                    ' Please check if the customer has a registered email '
                                    'address present in the database.'}, status=status.HTTP_400_BAD_REQUEST)


class SendSms(GenericAPIView):
    '''
    A generic API that allows you ro send an SMS
    to the currently logged in user or a different one.
    '''

    permission_classes = (IsAuthenticated,)
    serializer_classes = serializers.SmsSerializer

    def post(self, request, *aargs, **kwargs):

        if 'username_or_email' in list(request.data.keys()):
            if request.data.get('username_or_email') is not None:
                user = get.get_user(request.data.get('username_or_email'))
        else:
            user = request.user

        message = self.request.data.get("message")

        if user is not None and user.customer.has_mobile():
            communication.send_sms(str(user.customer.country_code) + str(user.customer.mobile), message)
            return Response({'message': 'Sms sent'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Sms could not be sent'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListEmails(ListCreateAPIView):
    '''
    Lists all the email objects.
    These are basically a log of all
    out bound emails.
    '''

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ListEmailSerializer
    queryset = Email.objects.all()
    filter_fields = "__all__"
    ordering_fields = "__all__"

    def post(self, request, *arg, **kwargs):

        if 'username_or_email' not in list(request.data.keys()):
            emails = models.Email.objects.all()
            return Response(serializers.EmailModelSerializer(emails, many=True).data, status=status.HTTP_200_OK)
        else:
            emails = self.get_user_email()
            if emails is not None:
                return Response(serializers.EmailModelSerializer(emails, many=True).data, status=status.HTTP_200_OK)
            else:
                return common.return_error("Error")

    def get_user_email(self):

        username_or_email = self.request.data.get("username_or_email")
        user = models.User.objects.filter(username=username_or_email).first()

        return models.Email.get_customer_mails(user) if user is not None else models.Email.objects.filter(
            to=username_or_email)


class RetrieveEmails(RetrieveAPIView):
    '''
    Retrieves a particular email object.
    '''

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.RetrieveEmailSerializer

    def get(self, request, *args, **kwargs):
        qs = models.Email.objects.filter(id=self.kwargs['pk']).first()

        if qs is not None:
            return super(RetrieveEmails, self).get(request, *args, **kwargs)
        return common.return_error("Object matching PK not found.")

    def get_object(self):
        return models.Email.objects.get(id=self.kwargs['pk'])


class ListSms(ListCreateAPIView):
    '''
    Lists all the SMS objects in the db.
    These are a log of all outbound SMS.
    '''

    # permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ListSmsSerializer
    queryset = SMS.objects.all()
    filter_fields = "__all__"
    ordering_fields = "__all__"

    def post(self, request, format=None):

        if 'username_or_email' not in list(request.data.keys()):
            sms = models.SMS.objects.all()
            return Response(serializers.SmsModelSerializer(sms, many=True).data, status=status.HTTP_200_OK)
        else:
            sms = self.get_user_sms()
            if sms is not None:
                return Response(serializers.SmsModelSerializer(sms, many=True).data, status=status.HTTP_200_OK)
            else:
                return common.return_error("Error")

    def get_user_sms(self):

        username_or_email = self.request.data.get("username_or_email")
        user = models.User.objects.filter(username=username_or_email).first()
        customer = Customer.objects.filter(email=username_or_email).first()

        return models.SMS.get_customer_sms(user) if user is not None else models.SMS.objects.filter(to=customer.mobile)


class RetrieveSms(RetrieveAPIView):
    '''
    Retrieve's a particular SMS object.
    '''

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.RetrieveSmsSerializer

    def get(self, request, *args, **kwargs):
        qs = models.SMS.objects.filter(id=self.kwargs['pk']).first()

        if qs is not None:
            return super(RetrieveSms, self).get(request, *args, **kwargs)
        return common.return_error("Object matching PK not found.")

    def get_object(self):
        return models.SMS.objects.get(id=self.kwargs['pk'])


class ListCreateEmailTemplateView(ListCreateAPIView):
    '''
    List all Email Templates available on GET. Creates an Email Template object on POST.
    '''

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.EmailTemplateSerializer
    queryset = models.EmailTemplate.objects.all()
    filter_fields = "__all__"
    ordering_fields = "__all__"


class RetrieveUpdateDestroyEmailTemplateView(RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, Update or Delete an Email Template object.
    '''

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.EmailTemplateSerializer
    queryset = models.EmailTemplate.objects.all()

    def get_object(self, *args, **kwargs):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('pk'))


class ListCreateSMSTemplateView(ListCreateAPIView):
    '''
    List all SMS Templates available on GET. Creates an SMS Template object on POST.
    '''

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SMSTemplateSerializer
    queryset = models.SmsTemplate.objects.all()
    filter_fields = "__all__"
    ordering_fields = "__all__"


class RetrieveUpdateDestroySMSTemplateView(RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, Update or Delete an SMS Template object.
    '''

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SMSTemplateSerializer
    queryset = models.SmsTemplate.objects.all()

    def get_object(self, *args, **kwargs):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('pk'))


class ViewEmailTemplate(TemplateView):
    template_name = "view-template.html"

    def get_html(self):
        from comms.models import EmailTemplate
        template = EmailTemplate.objects.get(id=self.kwargs.get("pk"))
        return template.body

