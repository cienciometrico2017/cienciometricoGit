# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0041_auto_20171206_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
