from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse("Hola, esto es una prueba")
