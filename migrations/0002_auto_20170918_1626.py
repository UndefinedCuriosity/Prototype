# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 23:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['-uploaded_at']},
        ),
    ]