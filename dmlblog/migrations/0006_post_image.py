# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmlblog', '0005_auto_20160930_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
