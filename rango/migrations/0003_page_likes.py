# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170125_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
