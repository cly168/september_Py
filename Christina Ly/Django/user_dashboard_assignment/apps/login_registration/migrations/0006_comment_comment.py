# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0005_auto_20160923_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]