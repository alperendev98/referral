# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-19 09:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import referral_project.admob_credentials.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdmobCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='Ad unit name')),
                ('appid', models.CharField(max_length=30, null=True, verbose_name='App id')),
                ('adunitid', models.CharField(max_length=30, null=True, verbose_name='Ad unit id')),
                ('adunittype', models.IntegerField(choices=[(0, 'Banner'), (1, 'Interstitial'), (2, 'Rewards')], default=referral_project.admob_credentials.fields.AdmobTypeOption(0))),
            ],
            options={
                'verbose_name': 'AdmobCredential',
                'verbose_name_plural': 'AdmobCredentials',
            },
        ),
    ]