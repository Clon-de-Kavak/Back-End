from django.db import models
from cars import models
from usuarios import models
class Venta(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField()
    user_id = models.IntegerField()
    

class Compra(models.Model):
    
    acount_id = models.IntegerField(primary_key =True)
    date = models.DateField()
    amount = models.FloatField()
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)