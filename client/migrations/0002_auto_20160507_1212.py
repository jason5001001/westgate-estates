# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-07 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contactable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='receive_news',
            field=models.BooleanField(default=False),
        ),
    ]