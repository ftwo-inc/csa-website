from __future__ import unicode_literals
from django.conf.urls import url, include

from comms import views

app_name = 'comms'
urlpatterns = [

    url(r'email/$', views.ListEmails.as_view(), name="list-email"),
    url(r'email/(?P<pk>\d+)$', views.RetrieveEmails.as_view(), name="retrieve-email"),

    url(r'email/template/(?P<pk>\d+)$', views.ViewEmailTemplate.as_view(), name="view-email-template"),


    url(r'sms/$', views.ListSms.as_view(), name="list-sms"),
    url(r'sms/(?P<pk>\d+)$', views.RetrieveSms.as_view(), name="retrieve-sms"),
    url(r'email/send/$', views.SendEmail.as_view(), name="send-email"),
    url(r'sms/send/$', views.SendSms.as_view(), name="send-sms"),

    url(r'sms/template/$', views.ListCreateSMSTemplateView.as_view(), name="list-create-sms-template"),
    url(r'sms/template/(?P<pk>\d+)$', views.RetrieveUpdateDestroySMSTemplateView.as_view(),
        name="retreive-update-destroy-sms-template"),
    url(r'email/template/$', views.ListCreateEmailTemplateView.as_view(), name="list-create-sms-template"),
    url(r'email/template/(?P<pk>\d+)$', views.RetrieveUpdateDestroyEmailTemplateView.as_view(),
        name="retreive-update-destroy-sms-template"),
]