# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-09 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('success', '0011_remove_articles_link_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='article_album',
        ),
    ]
