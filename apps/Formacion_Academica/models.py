# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from app.Investigador.models import investigador
class formacion_academica(models.Model):
 Nivel_Estudios=models.CharField(max_length=15)
 Fecha_Fin_Estudios=models.DateField()
 Nombre_Centro_Estudios=models.CharField(max_length=25)
 investigador = models.ForeignKey(investigador, null=True, blank=True, on_delete=models.CASCADE)