
from django.shortcuts import render,HttpResponse
import json

# Create your views here.
def hola_mundo(request):
    return HttpResponse("HolaaaaaAAaaAAaaaAA")

#si se seleciona ejemplo el carro 5 en la ruta, con el id debe demostrar el carro 5 
def qryId(request,carId):
    return HttpResponse(json.dumps({"id":carId, "nombre":"respuesta del carro"}), content_type="application/json")

def qryAll(request):
    return HttpResponse("All cars, aqui se retorna los objetos de todos los carros")


