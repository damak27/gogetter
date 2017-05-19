# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-13 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('success', '0017_auto_20170505_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='field',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]