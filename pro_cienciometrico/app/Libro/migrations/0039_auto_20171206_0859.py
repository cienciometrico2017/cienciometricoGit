# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libro', '0038_auto_20171206_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
