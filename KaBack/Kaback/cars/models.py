from django.db import models

# Create your models here.
class Car(models.Model):
    Precio =models.DecimalField(max_digits=6, decimal_places=2)
    Modelo = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100)
    Km = models.IntegerField()
    Ciudad =models.CharField(max_length=100)
    Transimisión = models.CharField(max_length=100)
    Tipo_auto = models.CharField(max_length=100)
    Color =  models.CharField(max_length=10)
    Combustible =  models.CharField(max_length=100)
    Pasajeros =  models.IntegerField()
    Estado = models.CharField(max_length= 100)
    Extras = models.CharDield ( max_length = 1000)