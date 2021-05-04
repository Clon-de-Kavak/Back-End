"""Kaback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cars import views as cars_views
from .router import car_router
from .router import user_router
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
  	path('hola-mundo/', cars_views.hola_mundo, name="hola_mundo"),
    path('api/',include(car_router.urls)),
    path('userapi/', include(user_router.urls)),
    path('api/token', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view())
]

###	path('cars/',  cars_views.qryAll, name="qryAll"),
###	path('cars/<int:carId>', cars_views.qryId, name="qryId")