# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-10 18:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20171206_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='day',
            field=models.DateField(default=datetime.datetime(2018, 2, 10, 18, 25, 3, 923516)),
        ),
    ]
