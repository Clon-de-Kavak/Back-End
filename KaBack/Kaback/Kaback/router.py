from rest_framework import routers
from cars.viewsets import CarViewSet
from usuarios.viewsets import UserViewSet

car_router = routers.DefaultRouter()
car_router.register("cars",CarViewSet)

user_router = routers.DefaultRouter()
user_router.register("user", UserViewSet)
