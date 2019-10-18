# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        from website.models import JobPosting, Testimonials
        ctx = super(HomePageView, self).get_context_data(*args, **kwargs)
        ctx["job_postings"] = JobPosting.objects.all()
        ctx["testimonials"] = Testimonials.objects.all()
        return ctx


class EnrollView(TemplateView):
    template_name = "enroll.html"

    def post(self, request):
        import pdb
        pdb.set_trace()


class AboutView(TemplateView):
    template_name = "about.html"


class PrivacyView(TemplateView):
    template_name = "privacy.html"


class IndustrySpeakView(TemplateView):
    template_name = "industry.html"


class FranchiseView(TemplateView):
    template_name = "franchise.html"


class ApplicationSecurityView(TemplateView):
    template_name = "course1.html"


class SecurityOperationCenterView(TemplateView):
    template_name = "course2.html"
