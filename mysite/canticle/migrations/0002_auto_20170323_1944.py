# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 00:44
from __future__ import unicode_literals

from django.db import migrations
from phonenumber_field.modelfields import PhoneNumberField

class Migration(migrations.Migration):

    dependencies = [
        ('canticle', '0001_initial'),
    ]

    operations = [
          migrations.AlterField('User','Phone_Number', PhoneNumberField())
    ]