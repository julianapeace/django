# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 19:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171130_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='author',
        ),
        migrations.RemoveField(
            model_name='student',
            name='level',
        ),
        migrations.DeleteModel(
            name='Level',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]