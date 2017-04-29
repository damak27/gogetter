# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-05 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('success', '0008_quotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='author_pic',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='articles',
            name='link_author',
            field=models.CharField(default='/', max_length=250),
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_hit',
            field=models.CharField(default='hit', max_length=300),
        ),
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.CharField(max_length=20),
        ),
    ]
