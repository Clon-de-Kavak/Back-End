from .models import Car
from .serializers import CarSerializerModel
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from decimal import Decimal as decimal

class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializerModel
    queryset = Car.objects.all()
    
    @action(detail=True,methods =["post"],url_path="add",url_name="add_car")
    def Add(self,request,pk=None):
        new_car= Car(
            Precio = decimal(request.query_params.get("precio")), 
            Modelo  = request.query_params.get("modelo"), 
            Marca = request.query_params.get("marca"), 
            Km  = int(request.query_params.get("km")), 
            Ciudad  = request.query_params.get("ciudad"),
            Transimisión  = request.query_params.get("transimision"), 
            Tipo_auto  = request.query_params.get("tipo_auto"), 
            Color  = request.query_params.get("color"), 
            Combustible  = request.query_params.get("combustible"), 
            Pasajeros  = int(request.query_params.get("pasajeros")), 
            Estado = request.query_params.get("estado"), 
            Extras = request.query_params.get("extras"))
        
        new_car.save()
        return Response(status=status.HTTP_201_CREATED)


