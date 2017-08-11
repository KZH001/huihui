# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 03:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20170719_1019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name'], 'verbose_name': '\u51fa\u7248\u793e', 'verbose_name_plural': '\u51fa\u7248\u793e'},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Publisher',
            new_name='publisher',
        ),
        migrations.AlterModelTable(
            name='publisher',
            table='publisher',
        ),
    ]
