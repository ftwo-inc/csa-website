# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class EnrollView(TemplateView):
    template_name = "enroll.html"


class AboutView(TemplateView):
    template_name = "about.html"


class PrivacyView(TemplateView):
    template_name = "privacy.html"


class IndustrySpeakView(TemplateView):
    template_name = "industry.html"
