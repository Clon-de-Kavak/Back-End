from rest_framework import routers
from cars.viewsets import CarViewSet

car_router = routers.DefaultRouter()
car_router.register("cars",CarViewSet)