# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Investigador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigador',
            name='Apellidos',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='Ciudadania',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='Nombres',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='Password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='investigador',
            name='cedula',
            field=models.CharField(max_length=12),
        ),
    ]