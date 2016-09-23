# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0003_auto_20160923_1008'),
        ('black_belt', '0002_auto_20160923_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='black_belt.Travel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_registration.User')),
            ],
        ),
    ]
