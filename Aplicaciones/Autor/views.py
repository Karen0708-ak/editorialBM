from django.shortcuts import render,redirect
from .models import Autor
from django.contrib import messages
def inicio(request):
    listadoAutor=Autor.objects.all()
    return render(request,"inicioau.html",{'autor':listadoAutor})

def nuevoAutor(request):
    return render(request,"nuevoAutor.html")
#Almacenando los datos de cargo en la Bdd
def guardarAutor(request):
    nombre = request.POST["nombre"]
    nacionalidad = request.POST["nacionalidad"]
    nuevoAutor=Autor.objects.create(
            nombre=nombre,
            nacionalidad=nacionalidad,
        )
    #mensaje de confirmacion
    messages.success(request,"Autor guardado exitosamente")
    return redirect('inicioau')
def eliminarAutor(request,id_autor):
    autorEliminar = Autor.objects.get(id=id)
    autorEliminar.delete()
    messages.success(request,"Autor ELIMINADO exitosamente")
    return redirect('inicioau')

#editar
def editarAutor(request,id):
    autorEditar=Autor.objects.get(id=id)
    return render(request,"editarAutor.html",{'autorEditar':autorEditar})

def procesarEdicionAutor(request):
    id_autor=request.POST["id_autor"]
    nombre = request.POST["nombre"]
    nacionalidad = request.POST["nacionalidad"]
    autor=autor.objects.get(id=id_autor)
    autor.nombre=nombre
    autor.nacionalidad=nacionalidad
    autor.save()
    #mensaje de confirmacion
    messages.success(request,"Autor ACTUALIZADO exitosamente")
    return redirect('inicioau')