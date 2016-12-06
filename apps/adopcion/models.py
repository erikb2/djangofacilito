from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre    = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=30)
    edad      = models.IntegerField()
    telefono  = models.CharField(max_length=12)
    domicilio = models.TextField()

