# Generated by Django 2.2 on 2019-10-12 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='link',
            field=models.CharField(default=django.utils.timezone.now, max_length=220),
            preserve_default=False,
        ),
    ]