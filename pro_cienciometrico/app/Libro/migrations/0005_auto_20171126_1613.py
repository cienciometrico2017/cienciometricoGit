# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Libro', '0004_auto_20171126_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='Editorial',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='libro',
            name='ISBN',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='libro',
            name='Titulo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='libro',
            name='Ubicacion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='libro',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]
