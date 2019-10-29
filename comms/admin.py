from __future__ import unicode_literals
from django.contrib import admin
from django.apps import apps
from comms import models
from comms import resources
from import_export.admin import ImportExportMixin

app = apps.get_app_config('comms')

for model_name, model in list(app.models.items()):
    admin.site.register(model)


class EmailResourceAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = resources.EmailResource


admin.site.unregister(models.Email)
admin.site.register(models.Email, EmailResourceAdmin)


class SmsResourceAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = resources.SmsResource


admin.site.unregister(models.SMS)
admin.site.register(models.SMS, SmsResourceAdmin)


class EmailTemplateResourceAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = resources.EmailTemplateResource
    list_display = ['id', 'subject', 'slug']


admin.site.unregister(models.EmailTemplate)
admin.site.register(models.EmailTemplate, EmailTemplateResourceAdmin)


class SmsTemplateResourceAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = resources.SmsTemplateResource
    list_display = ['id', 'slug']


admin.site.unregister(models.SmsTemplate)
admin.site.register(models.SmsTemplate, SmsTemplateResourceAdmin)
