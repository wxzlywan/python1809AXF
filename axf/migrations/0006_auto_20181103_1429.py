# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-03 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0005_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='specifics',
            field=models.CharField(max_length=100),
        ),
    ]
