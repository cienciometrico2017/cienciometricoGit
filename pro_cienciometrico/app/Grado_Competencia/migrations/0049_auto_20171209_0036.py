# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 05:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grado_Competencia', '0048_auto_20171209_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grado_competencia',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]
