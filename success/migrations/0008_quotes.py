# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-02 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('success', '0007_auto_20170402_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(default='Did you also know ,success is not determine by the number of certificates you acquire in life.', max_length=2000)),
                ('quote_by', models.CharField(default='ebong', max_length=250)),
            ],
        ),
    ]
