from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('website')

for model_name, model in list(app.models.items()):
    admin.site.register(model)
