# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Privilegios', '0040_auto_20171204_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privilegios',
            name='investigador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Investigador.investigador'),
        ),
    ]
