# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-16 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apkstore', '0006_auto_20180316_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apkdetails',
            name='apk_version',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apksubdetails',
            name='apk_version',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
