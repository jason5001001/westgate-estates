# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('westgate_estates', '0002_auto_20160408_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residential',
            name='AGENT_REF',
            field=models.CharField(max_length=52, unique=True),
        ),
        migrations.AlterField(
            model_name='residential',
            name='POSTCODE1',
            field=models.CharField(max_length=52),
        ),
        migrations.AlterField(
            model_name='residential',
            name='POSTCODE2',
            field=models.CharField(max_length=52),
        ),
    ]
