# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos_Cientificos', '0016_auto_20171129_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos_cientificos',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]