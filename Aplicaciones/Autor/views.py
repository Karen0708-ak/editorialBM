from django.shortcuts import render
from .models import Autor

def inicio(request):
    listadoAutor=Autor.objects.all()
    return render(request,"inicioau.html",{'autor':listadoAutor})