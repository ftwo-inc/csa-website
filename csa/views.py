from __future__ import unicode_literals
from rest_framework import status
from django.views.generic import TemplateView, View

from django.views import generic
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from rest_framework.views import APIView
import datetime
from django.db.models import Q
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout


class DashboardView(LoginRequiredMixin, generic.ListView):
    template_name = "../templates/dashboard/dashboard.html"
