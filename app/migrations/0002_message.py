# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 21:26
from __future__ import unicode_literals

import app.models.Message.message
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_id', models.IntegerField()),
                ('receiver_id', models.IntegerField()),
                ('message', models.TextField(max_length=65535)),
                ('read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]