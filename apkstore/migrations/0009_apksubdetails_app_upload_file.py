# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apkstore', '0008_apkdetails_app_upload_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='apksubdetails',
            name='app_upload_file',
            field=models.FileField(blank=True, null=True, upload_to=b'apkfile'),
        ),
    ]
