# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-13 18:49
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20180413_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='reward',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), max_digits=10),
        ),
    ]