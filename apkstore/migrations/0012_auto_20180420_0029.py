# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-19 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apkstore', '0011_auto_20180420_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apkdetails',
            old_name='apk_url',
            new_name='apk_hostgetor_url',
        ),
        migrations.RenameField(
            model_name='apksubdetails',
            old_name='apk_url',
            new_name='apk_hostgetor_url',
        ),
    ]
