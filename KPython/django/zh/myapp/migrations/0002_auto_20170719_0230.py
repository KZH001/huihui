# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='website',
        ),
        migrations.AddField(
            model_name='author',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
