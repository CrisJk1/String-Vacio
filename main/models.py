from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Acciones(models.Model):
    Accion = models.CharField(max_length=50)
    Categoria = models.CharField(max_length=50)
    Acumulable = models.BooleanField()
    Huella = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.Accion + "-" + self.Categoria

class RegistroCO(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Fecha = models.DateField(auto_now_add=True)
    Repositorio = models.DecimalField(max_digits=6,decimal_places=2,default = 0)

    def __str__(self):
        return self.Fecha + "-" + self.Usuario

class Configuracion(models.Model):
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Preferencias = models.CharField(default="t,")
    Deuda = models.DecimalField(max_digits=6,decimal_places=2,default=4400.00)

    def __str__(self):
        return self.Usuario.username

