from django.shortcuts import render,redirect
from .models import Investigador
from django.contrib import messages
def inicio(request):
    listadoInvestigador=Investigador.objects.all()
    return render(request,"investigador.html",{'investigador':listadoInvestigador})

def nuevoInvestigador(request):
    return render(request,"nuevoInvestigador.html")

def guardarInvestigador(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    nacionalidad = request.POST["nacionalidad"]
    edad = request.POST["edad"]
    nuevoInvestigador=Investigador.objects.create(
            nombre=nombre,
            nacionalidad=nacionalidad,
            apellido=apellido,
            edad=edad
        )
    messages.success(request,"Investigador guardado exitosamente")
    return redirect('investigador')

def eliminarInvestigador(request,id_investigador):
    InvestigadorEliminar = Investigador.objects.get(id_investigador=id_investigador)
    InvestigadorEliminar.delete()
    messages.success(request,"Investigador ELIMINADO exitosamente")
    return redirect('investigador')

def editarInvestigador(request,id_investigador):
    investigadorEditar=Investigador.objects.get(id_investigador=id_investigador)
    return render(request,"editarInvestigador.html",{'investigadorEditar':investigadorEditar})

def procesarEdicionInvestigador(request):
    id_investigador=request.POST["id_investigador"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    nacionalidad = request.POST["nacionalidad"]
    edad = request.POST["edad"]
    autor=Investigador.objects.get(id_investigador=id_investigador)
    autor.nombre=nombre
    autor.apellido=apellido
    autor.nacionalidad=nacionalidad
    autor.edad=edad
    autor.save()
    messages.success(request,"Investigador ACTUALIZADO exitosamente")
    return redirect('investigador')