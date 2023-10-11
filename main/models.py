from django.db import models

# Create your models here.

class Acciones(models.Model):
    Accion = models.CharField(max_length=50)
    Categoria = models.CharField(max_length=50)
    Acumulable = models.BooleanField()
    Huella = models.IntegerField()

class Usuarios(models.Model):
    Usuario = models.CharField(max_length=20)
    Correo = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=50)

class RegistroCO(models.Model):
    Usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Fecha = models.DateTimeField(auto_now_add=True)
    Repositorio = models.CharField()

