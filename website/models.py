from __future__ import unicode_literals

from django.db import models


class JobPosting(models.Model):
    logo = models.FileField()
    link = models.CharField(max_length=220)
    title = models.CharField(max_length=220)
    location = models.CharField(max_length=220)
    description = models.CharField(max_length=220)


class Testimonials(models.Model):
    pic = models.FileField()
    content = models.CharField(max_length=440)
    name = models.CharField(max_length=220)
    company = models.CharField(max_length=220)
    logo = models.FileField()


class Franchise(models.Model):
    fullname = models.CharField(max_length=220)
    email = models.EmailField(max_length=220)
    mobile = models.CharField(max_length=220)


class Enroll(models.Model):
    fullname = models.CharField(max_length=220)
    email = models.EmailField(max_length=220)
    mobile = models.CharField(max_length=220)
