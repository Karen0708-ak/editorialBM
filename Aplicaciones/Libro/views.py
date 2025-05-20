from django.shortcuts import render,redirect

# Create your views here.
#importando el modelo plato
from .models import Libro
from django.contrib import messages
#esta función es para renderizar el listado de Plato
def inicio(request):
    listadoLibro=Libro.objects.all()
    return render(request,"iniciobo.html",{'libro':listadoLibro})
