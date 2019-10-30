# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, JsonResponse

import logging
logging.getLogger(__name__)


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        from website.models import JobPosting, Testimonials, PopupFrame
        ctx = super(HomePageView, self).get_context_data(*args, **kwargs)
        ctx["job_postings"] = JobPosting.objects.all()
        ctx["testimonials"] = Testimonials.objects.all()
        ctx["popup_frame"] = PopupFrame.objects.all()
        return ctx


class EnrollView(TemplateView):
    template_name = "enroll.html"

    def post(self, request, *args, **kwargs):
        from website.models import Enroll
        enroll = Enroll.objects.create(
            fullname=self.request.POST.get("fullname"),
            email=self.request.POST.get("email"),
            mobile=self.request.POST.get("mobile"),
            location=self.request.POST.get("location"),
            comment=self.request.POST.get("comment")
        )
        try:
            enroll.send_notifications("enroll-submit-to-customer")
            enroll.send_notifications("enroll-submit-to-admin")
        except Exception as e:
            logging.error(e)
        return JsonResponse({"status": True, "message": ""})


class AboutView(TemplateView):
    template_name = "about.html"


class PrivacyView(TemplateView):
    template_name = "privacy.html"


class IndustrySpeakView(TemplateView):
    template_name = "industry.html"

    def get_context_data(self, *args, **kwargs):
        from website.models import NewsAndUpdates
        ctx = super(IndustrySpeakView, self).get_context_data(*args, **kwargs)
        ctx["news_and_update"] = NewsAndUpdates.objects.all()
        return ctx


class FranchiseView(TemplateView):
    template_name = "franchise.html"

    def post(self, request, *args, **kwargs):
        from website.models import Franchise
        franchise = Franchise.objects.create(
            fullname=self.request.POST.get("fullname"),
            email=self.request.POST.get("email"),
            mobile=self.request.POST.get("mobile"),
            location=self.request.POST.get("location"),
            comment=self.request.POST.get("comment")
        )
        try:
            franchise.send_notifications("franchise-submit-to-customer")
            franchise.send_notifications("franchise-submit-to-admin")
        except Exception as e:
            logging.error(e)
        return JsonResponse({"status": True, "message": ""})


class ApplicationSecurityView(TemplateView):
    template_name = "course1.html"


class SecurityOperationCenterView(TemplateView):
    template_name = "course2.html"
