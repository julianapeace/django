# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chungtai', '0008_auto_20171130_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='static/uploads/%Y/%m/%d/')),
            ],
        ),
    ]