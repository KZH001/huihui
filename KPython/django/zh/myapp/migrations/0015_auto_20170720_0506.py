# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 05:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20170720_0400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '\u4f5c\u8005', 'verbose_name_plural': '\u4f5c\u8005'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title'], 'verbose_name': '\u4e66', 'verbose_name_plural': '\u4e66'},
        ),
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]