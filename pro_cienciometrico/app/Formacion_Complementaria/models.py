# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from app.Investigador.models import investigador

class formacion_complementaria(models.Model):
    Nivel_Estudios=models.CharField(max_length=20)
    Fecha_Fin=models.DateField()
    Nombre_Centro_Estudios=models.CharField(max_length=50)
    investigador=models.ForeignKey(investigador,null=True ,blank=True,on_delete=models.CASCADE)

    def __str__(self): return '{}'.format(self.Nivel_Estudios)