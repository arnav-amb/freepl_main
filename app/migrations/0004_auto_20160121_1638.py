# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 16:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160120_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='day',
            field=models.DateField(default=datetime.datetime(2016, 1, 21, 16, 38, 57, 185050)),
        ),
    ]