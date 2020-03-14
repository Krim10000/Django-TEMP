# -*- coding: utf-8 -*-
from django.db import models

class T_Vs_t(models.Model): # crea el modelo que guarda temperatura y fecha
    TEMPERATURA=models.FloatField() # temp como float ej 24,01
    FECHA= models.DateTimeField(auto_now_add=True) # la fecha es automatica cuando se registra una temp

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return '%s:  %s' % (self.FECHA, self.TEMPERATURA,)
