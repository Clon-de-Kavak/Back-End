from django.db import models
from cars.models import Car as car
from usuarios.models import Usuario as usi
class Venta(models.Model):
    car_id = models.ForeignKey(car,on_delete=models.PROTECT)
    fecha = models.DateField()
    precio= models.FloatField()
    usuario_id = models.ForeignKey(usi,on_delete=models.PROTECT)

class Compra(models.Model):
    
    usuario_id = models.ForeignKey(usi,on_delete=models.PROTECT)
    fecha = models.DateField()
    precio = models.FloatField()
    car_id = models.ForeignKey(car,on_delete=models.PROTECT)
