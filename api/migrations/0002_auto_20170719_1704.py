# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceevent',
            name='userid',
            field=models.CharField(blank=True, max_length=1000, unique=True),
        ),
    ]
