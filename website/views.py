# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from django.views.generic import TemplateView
from django.views import generic
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView


class HomePageView(TemplateView):
    template_name = "home.html"


class CourseView(TemplateView):
    template_name = "course.html"


class AboutView(TemplateView):
    template_name = "about.html"


class PrivacyView(TemplateView):
    template_name = "privacy.html"
