# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zona',
            name='Descripcion',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='zona',
            name='Nombre',
            field=models.CharField(max_length=50),
        ),
    ]
