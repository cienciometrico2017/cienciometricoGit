# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facultad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultad',
            name='Decano',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='facultad',
            name='Nombre',
            field=models.CharField(max_length=100),
        ),
    ]
