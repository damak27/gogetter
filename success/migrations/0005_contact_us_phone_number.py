# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-29 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('success', '0004_contact_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='phone_number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
