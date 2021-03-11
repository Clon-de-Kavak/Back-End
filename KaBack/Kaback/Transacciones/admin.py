from django.contrib import admin
from Transacciones import models

admin.site.register(models.Venta)
admin.site.register(models.Compra)

# Register your models here.