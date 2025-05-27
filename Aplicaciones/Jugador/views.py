from django.shortcuts import render,redirect
from .models import Jugador
from django.contrib import messages
def inicio(request):
    listadoJugador=Jugador.objects.all()
    return render(request,"inicioju.html",{'jugador':listadoJugador})

def nuevoJugador(request):
    return render(request,"nuevoJugador.html")
#Almacenando los datos de cargo en la Bdd
def guardarJugador(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    celular = request.POST["celular"]
    nuevoJugador=Jugador.objects.create(
            nombre=nombre,
            apellido=apellido,
            celular=celular
        )
    #mensaje de confirmacion
    messages.success(request,"Jugador guardado exitosamente")
    return redirect('inicioju')
def eliminarJugador(request,id_jugador):
    jugadorEliminar = Jugador.objects.get(id_jugador=id_jugador)
    jugadorEliminar.delete()
    messages.success(request,"Jugador ELIMINADO exitosamente")
    return redirect('inicioju')

#editar
def editarJugador(request,id_jugador):
    jugadorEditar=Jugador.objects.get(id_jugador=id_jugador)
    return render(request,"editarJugador.html",{'jugadorEditar':jugadorEditar})

def procesarEdicionJugador(request):
    id_jugador=request.POST["id_jugador"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    celular = request.POST["celular"]
    jugador = Jugador.objects.get(id_jugador=id_jugador)
    jugador.nombre=nombre
    jugador.apellido=apellido
    jugador.celular=celular
    jugador.save()
    #mensaje de confirmacion
    messages.success(request,"Jugador ACTUALIZADO exitosamente")
    return redirect('inicioju')