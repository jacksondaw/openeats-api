# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-11 14:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_groups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='author',
        ),
    ]
