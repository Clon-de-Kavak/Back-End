from django.db import models
from cars.models import Car as cars
# Create your models here.

class Usuario(models.Model):
    Nombre = models.CharField(max_length=20)
    Telefono = models.CharField(max_length=12)
    Correo_Electronico = models.CharField(max_length=50)
    Rol = models.CharField(max_length = 10)
    


class Favorito(models.Model):
    coche = models.ForeignKey(cars,on_delete = models.CASCADE )
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)