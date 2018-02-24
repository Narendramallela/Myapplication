# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-04 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('canticle', '0002_auto_20180204_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicinterest',
            name='Created_Date',
        ),
        migrations.AddField(
            model_name='musicinterest',
            name='Timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musicinterest',
            name='Updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]