# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 17:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171130_1715'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Levels',
            new_name='Level',
        ),
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]