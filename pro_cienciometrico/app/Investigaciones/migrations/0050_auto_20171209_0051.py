# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Investigaciones', '0049_auto_20171209_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigaciones',
            name='investigador',
            field=models.ManyToManyField(to='Investigador.investigador'),
        ),
    ]
