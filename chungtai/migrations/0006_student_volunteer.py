# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chungtai', '0005_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='volunteer',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
