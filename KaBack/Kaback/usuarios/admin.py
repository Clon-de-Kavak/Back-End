from django.contrib import admin
from usuarios import models

admin.site.register(models.Usuario)
admin.site.register(models.Favorito)

# Register your models here.