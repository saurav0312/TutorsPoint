# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_remove_member_member_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='member1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reg_no', models.CharField(max_length=8)),
                ('sruname', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=1000)),
            ],
        ),
    ]
