# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0003_auto_20160921_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
