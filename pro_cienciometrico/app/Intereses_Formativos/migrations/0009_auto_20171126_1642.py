# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Intereses_Formativos', '0008_auto_20171126_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intereses_formativos',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]
