# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish_bowl_monitor', '0003_auto_20170921_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanktemp',
            name='weather_data_temp',
            field=models.FloatField(blank=True, null=True),
        ),
    ]