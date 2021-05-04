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
            Transmision  = request.query_params.get("transmision"), 
            Tipo_auto  = request.query_params.get("tipo_auto"), 
            Color  = request.query_params.get("color"), 
            Combustible  = request.query_params.get("combustible"), 
            Pasajeros  = int(request.query_params.get("pasajeros")), 
            Estado = request.query_params.get("estado"), 
            Extras = request.query_params.get("extras"))
        
        new_car.save()
        return Response(status=status.HTTP_201_CREATED)

    @action(detail = True, methods = ["update"], url_path= "update", url_name = "update_car")
    def UpdateCar(self,request, pk = None):
       # Actu = Car.objects.get(id=request.query_params.get("id"))
        camp = request.query_params.get("campo")
        valor = request.query_params.get("value")
        Car.objects.get(id=request.query_params.get("id")).update({campo:valor}).save()
        return Response(status=status.HTTP_202_ACCEPTED)

        #if request.query_params.get("campo") == "precio":
         #   Actu.Precio 

    @action(detail = True, methods = ["delete"], url_path= "delete", url_name = "delete_car")
    def DeleteCar(self,request, pk = None):
        id_coche = Car.objects.get(id=request.query_params.get("id"))
        Car.objects.get(id = id_coche).delete()
        return Response(status=status.HTTP_200_OK)

        #if request.query_params.get("campo") == "precio":
         #   Actu.Precio 