# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chungtai', '0009_class_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='class_material',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class_material',
            name='upload',
            field=models.FileField(upload_to='uploads/%Y/%m/%d/'),
        ),
    ]