# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0005_auto_20171125_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]
