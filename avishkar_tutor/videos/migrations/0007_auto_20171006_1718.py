# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 11:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20171006_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='c',
            old_name='videosource',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='java',
            old_name='videosource',
            new_name='course',
        ),
    ]
