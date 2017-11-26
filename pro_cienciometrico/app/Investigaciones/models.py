# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from  app.Investigador.models import investigador

class investigaciones (models.Model):
    Titulo=models.CharField(max_length=50)
    investigador=models.ForeignKey(investigador,null=True ,blank=True,on_delete=models.CASCADE)
    Palabras_Clave=models.TextField(200),
    Resumen= models.FileField()
    Fecha=models.DateField()
    Editor=models.CharField(max_length=50)
    Url=models.URLField()

    def __str__(self): return '{}'.format(self.Titulo)