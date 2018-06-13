# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-28 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apkstore', '0019_auto_20180422_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apkdetails',
            name='description_1',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='apkdetails',
            name='description_2',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='apkdetails',
            name='description_3',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='apkdetails',
            name='description_4',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='apkdetails',
            name='meta_description',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AlterField(
            model_name='apkdetails',
            name='meta_keyword',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AlterField(
            model_name='apkdetails',
            name='page_title',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AlterField(
            model_name='apksubdetails',
            name='description_1',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='apksubdetails',
            name='description_2',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='apksubdetails',
            name='description_3',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='apksubdetails',
            name='description_4',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='apksubdetails',
            name='meta_description',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AlterField(
            model_name='apksubdetails',
            name='meta_keyword',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AlterField(
            model_name='apksubdetails',
            name='page_title',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]
