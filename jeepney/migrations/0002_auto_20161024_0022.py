# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 16:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeepney', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='description',
            new_name='place',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='routes',
        ),
        migrations.RemoveField(
            model_name='item',
            name='amount',
        ),
    ]
