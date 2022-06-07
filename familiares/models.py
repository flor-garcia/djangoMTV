from django.db import models
from datetime import datetime

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.FloatField()
    fecha_nacimiento = models.CharField(max_length=20)
    parentesco = models.CharField(max_length=40, null=True, blank=True)
    