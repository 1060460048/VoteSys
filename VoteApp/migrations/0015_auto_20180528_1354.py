# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-28 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoteApp', '0014_uservoterecord_uremark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservoterecord',
            name='uRemark',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
