# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-08 07:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('early', '0005_auto_20161108_0704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='early',
            old_name='comments',
            new_name='comment',
        ),
    ]
