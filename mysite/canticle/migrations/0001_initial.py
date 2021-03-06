# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-27 02:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Artists', models.CharField(max_length=200)),
                ('Album_Name', models.CharField(max_length=200)),
                ('Created_Date', models.DateTimeField(verbose_name='auto_now_add=True')),
                ('Link', models.CharField(max_length=100)),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Website_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Allowed_Flag', models.CharField(max_length=100)),
                ('Link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canticle.Song')),
            ],
        ),
    ]
