from django.db import models

# Create your models here.

class objetivos(models.Model):
    accion = models.CharField(max_length=30)
    huella = models.IntegerField()
    informacion = models.CharField(max_length=400)

class Usuarios(models.Model):
    Usuario = models.CharField(max_length=20)
    Correo = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=50)

class RegistroCO(models.Model):
    Usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Fecha = models.DateTimeField(auto_now_add=True)
    Repositorio = models.CharField()

