# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 01:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Unidad_Investigacion', '0001_initial'),
        ('Ambito_Investigativo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambito_investigativo',
            name='unidad_investigacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Unidad_Investigacion.unidad_investigacion'),
        ),
    ]