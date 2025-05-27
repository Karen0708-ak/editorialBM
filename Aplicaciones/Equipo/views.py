from .models import Equipo
from .models import Jugador
from django.shortcuts import render, redirect
from django.contrib import messages
def inicio(request):
    listadoEquipo=Equipo.objects.all()
    return render(request,"inicioeq.html",{'equipo':listadoEquipo})

def nuevoEquipo(request):
    rjugador=Jugador.objects.all()
    return render(request,"nuevoEquipo.html",{'jugador':rjugador})
#Almacenando los datos de cargo en la Bdd
def guardarEquipo(request):
    nombre = request.POST["nombre"]
    partidos_ganados = request.POST["partidos_ganados"]
    partidos_perdidos = request.POST["partidos_perdidos"]
    jugadores_ids = request.POST.getlist("jugador")
    nuevoEquipo=Equipo.objects.create(
            nombre=nombre,
            partidos_ganados=partidos_ganados,
            partidos_perdidos=partidos_perdidos,

        )
    for jugador_id in jugadores_ids:
            jugador = Jugador.objects.get(id_jugador=jugador_id)
            nuevoEquipo.jugador.add(jugador)
    #mensaje de confirmacion
    messages.success(request,"Equipo guardado exitosamente")
    return redirect('inicioeq')

def eliminarEquipo(request,id_equipo):
    equipoEliminar = Equipo.objects.get(id_equipo=id_equipo)
    equipoEliminar.delete()
    messages.success(request,"Equipo ELIMINADO exitosamente")
    return redirect('inicioeq')

#editar
def editarEquipo(request,id_equipo):
    equipoEditar=Equipo.objects.get(id_equipo=id_equipo)
    rjugador=Jugador.objects.all()
    jugadores_actuales = equipoEditar.jugador.values_list('id_jugador', flat=True)
    return render(request, "editarEquipo.html", {
        'equipoEditar': equipoEditar,
        'jugador': rjugador,
        'jugadores_actuales': jugadores_actuales
    })

def procesarEdicionEquipo(request):
    id_equipo=request.POST["id_equipo"]
    nombre = request.POST["nombre"]
    partidos_ganados = request.POST["partidos_ganados"]
    partidos_perdidos = request.POST["partidos_perdidos"]
    jugadores_ids = request.POST.getlist("jugador")
    equipo=Equipo.objects.get(id_equipo=id_equipo)
    equipo.nombre=nombre
    equipo.partidos_ganados=partidos_ganados
    equipo.partidos_perdidos=partidos_perdidos
   
    equipo.save()

     # Actualizamos jugadores (primero limpiamos)
    equipo.jugador.clear()
    for jugador_id in jugadores_ids:
        jugador = Jugador.objects.get(id_jugador=jugador_id)
        equipo.jugador.add(jugador)
    #mensaje de confirmacion
    messages.success(request,"Equipo ACTUALIZADO exitosamente")
    return redirect('inicioeq')