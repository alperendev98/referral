# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-16 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0005_campaign_max_interactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='max_interactions',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Maximum Allowed Interactions'),
        ),
    ]
