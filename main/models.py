from django.db import models

# Create your models here.

class objetivos(models.Model):
    accion = models.CharField(max_length=30)
    huella = models.IntegerField()
    informacion = models.CharField(max_length=400)
