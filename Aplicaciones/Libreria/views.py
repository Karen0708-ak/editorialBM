from django.shortcuts import render,redirect
from .models import Libreria
from django.contrib import messages

def inicio(request):
    listadoLibreria=Libreria.objects.all()
    return render(request,"inicioli.html",{'libreria':listadoLibreria})

def nuevaLibreria(request):
    return render(request,"nuevaLibreria.html")
#Almacenando los datos de cargo en la Bdd
def guardarLibreria(request):
    nombre = request.POST["nombre"]
    direccion= request.POST["direccion"]
    nuevaLibreria=Libreria.objects.create(
            nombre=nombre,
            direccion=direccion,
        )
    #mensaje de confirmacion
    messages.success(request,"Libreria guardado exitosamente")
    return redirect('inicioli')
def eliminarLibreria(request,id_libreria):
    libreriaEliminar = Libreria.objects.get(id_libreria=id_libreria)
    libreriaEliminar.delete()
    messages.success(request,"Libreria ELIMINADA exitosamente")
    return redirect('inicioli')

#editar
def editarLibreria(request,id_libreria):
    libreriaEditar=Libreria.objects.get(id_libreria=id_libreria)
    return render(request,"editarLibreria.html",{'libreriaEditar':libreriaEditar})

def procesarEdicionLibreria(request):
    id_libreria=request.POST["id_libreria"]
    nombre = request.POST["nombre"]
    direccion = request.POST["direccion"]
    libreria=Libreria.objects.get(id_autor=id_libreria)
    libreria.nombre=nombre
    libreria.direccion=direccion
    libreria.save()
    #mensaje de confirmacion
    messages.success(request,"Libreria ACTUALIZADA exitosamente")
    return redirect('inicioli')