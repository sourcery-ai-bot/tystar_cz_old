# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-04 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0007_auto_20170904_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='csfd',
            field=models.URLField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='actor',
            name='imdb',
            field=models.URLField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]