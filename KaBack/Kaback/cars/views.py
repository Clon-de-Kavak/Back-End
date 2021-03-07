
from django.shortcuts import render,HttpResponse
# Create your views here.
def hola_mundo(request):
    return HttpResponse("HolaaaaaAAaaAAaaaAA")

#si se seleciona ejemplo el carro 5 en la ruta, con el id debe demostrar el carro 5 
def qryId(request,carId):
    return HttpResponse("Id")

def qryAll(request):
    return HttpResponse("All cars, aqui se retorna los objetos de todos los carros")


