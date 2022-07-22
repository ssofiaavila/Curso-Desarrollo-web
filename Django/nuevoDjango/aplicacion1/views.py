from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1(request): #lo que hará cuando se ejecute una petición
    return HttpResponse("Hola, bienvenido")
