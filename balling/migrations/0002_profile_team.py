# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('balling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='team', to='balling.Teams'),
            preserve_default=False,
        ),
    ]
