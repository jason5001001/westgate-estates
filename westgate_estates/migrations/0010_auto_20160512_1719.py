# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('westgate_estates', '0009_auto_20160511_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='save_search',
            name='r_high_bedroom',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='save_search',
            name='r_high_price',
            field=models.FloatField(default=99999),
        ),
        migrations.AlterField(
            model_name='save_search',
            name='r_low_bedroom',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='save_search',
            name='r_low_price',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='save_search',
            name='s_high_bedroom',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='save_search',
            name='s_high_price',
            field=models.FloatField(default=99999),
        ),
        migrations.AlterField(
            model_name='save_search',
            name='s_low_bedroom',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='save_search',
            name='s_low_price',
            field=models.FloatField(default=100),
        ),
    ]
