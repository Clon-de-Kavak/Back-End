from .models import Usuario
from .serializers import UserSerializerModel
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from decimal import Decimal as decimal

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializerModel
    queryset = Usuario.objects.all()
    
    @action(detail=True,methods =["post"],url_path="add",url_name="add_user")
    def Add(self,request,pk=None):
      
          new_user = Usuario(
               Nombre = (request.query_params.get("nombre")),
               Telefono = (request.query_params.get("telefono")),
               Correo_Electronico = (request.query_params.get("marca")),
               Rol = (request.query_params.get("rol"))
          )
          new_user.save()
          return Response(status=status.HTTP_201_CREATED)

    @action(detail = True, methods = ["update"], url_path= "update", url_name = "update_user")
    def UpdateUser(self,request, pk = None):
        camp = request.query_params.get("campo")
        valor = request.query_params.get("value")
        Usuario.objects.get(id=request.query_params.get("id")).update({campo:valor}).save()
        return Response(status=status.HTTP_202_ACCEPTED)


    @action(detail = True, methods = ["delete"], url_path= "delete", url_name = "delete_user")
    def DeleteUser(self,request, pk = None):
        id_user = User.objects.get(id=request.query_params.get("id"))
        Usuario.objects.get(id = id_user).delete()
        return Response(status=status.HTTP_200_OK)
