# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-16 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0007_auto_20180916_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='pre_url',
            field=models.URLField(blank=True, null=True, verbose_name='Pre url for web traffic ads only'),
        ),
    ]