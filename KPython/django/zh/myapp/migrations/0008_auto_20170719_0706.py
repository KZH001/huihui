# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20170719_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(default=12, null=True),
        ),
    ]