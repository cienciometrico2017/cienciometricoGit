# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 01:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Investigaciones', '0002_auto_20171120_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigaciones',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]
