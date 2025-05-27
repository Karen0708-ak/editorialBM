from django.shortcuts import render, redirect, get_object_or_404
from .models import Libros
from Aplicaciones.investigador.models import Investigador  # importa desde el lugar correcto si es otro

def inicio(request):
    libross = Libros.objects.all()
    return render(request, 'libros.html', {'libross': libross})

def nuevosLibros(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        anio = request.POST.get('anio')
        ISBN = request.POST.get('ISBN')
        paginas = request.POST.get('paginas')
        investigador_id = request.POST.get('investigador')

        investigador = get_object_or_404(Investigador, id_investigador=investigador_id)

        libro = Libros(titulo=titulo, anio=anio, ISBN=ISBN, paginas=paginas, investigadores=investigador)
        libro.save()
        return redirect('inicio')
    
    investigadores = Investigador.objects.all()
    return render(request, 'nuevosLibros.html', {'investigadores': investigadores})

from django.db import IntegrityError
from django.contrib import messages  # Opcional para enviar mensajes a la plantilla

def guardarLibros(request):
    if request.method == 'POST':
        libro_id = request.POST.get('id')  # Para saber si es edición o creación
        titulo = request.POST.get('titulo')
        anio = request.POST.get('anio')
        ISBN = request.POST.get('ISBN')
        paginas = request.POST.get('paginas')
        investigador_id = request.POST.get('investigador')

        investigador = Investigador.objects.get(id_investigador=investigador_id)

        if libro_id:  # Edición
            libro = Libros.objects.get(id=libro_id)
            # Verificar si hay otro libro con el mismo ISBN
            if Libros.objects.exclude(id=libro_id).filter(ISBN=ISBN).exists():
                messages.error(request, "Ya existe otro libro con ese ISBN.")
                investigadores = Investigador.objects.all()
                return render(request, 'editarLibros.html', {'libro': libro, 'investigadores': investigadores})

            # Actualizar datos
            libro.titulo = titulo
            libro.anio = anio
            libro.ISBN = ISBN
            libro.paginas = paginas
            libro.investigadores = investigador
            libro.save()

        else:  # Creación
            if Libros.objects.filter(ISBN=ISBN).exists():
                messages.error(request, "Ya existe un libro con ese ISBN.")
                investigadores = Investigador.objects.all()
                return render(request, 'nuevosLibros.html', {'investigadores': investigadores})

            libro = Libros(titulo=titulo, anio=anio, ISBN=ISBN, paginas=paginas, investigadores=investigador)
            libro.save()

        return redirect('inicio')

    # GET request, redirigir o mostrar error si necesario
    return redirect('inicio')


def editarLibros(request, id):
    libro = get_object_or_404(Libros, pk=id)
    if request.method == 'POST':
        libro.titulo = request.POST.get('titulo')
        libro.anio = request.POST.get('anio')
        libro.ISBN = request.POST.get('ISBN')
        libro.paginas = request.POST.get('paginas')
        investigador_id = request.POST.get('investigador')
        libro.investigadores = get_object_or_404(Investigador, id_investigador=investigador_id)
        libro.save()
        return redirect('inicio')
    
    investigadores = Investigador.objects.all()
    return render(request, 'editarLibros.html', {'libro': libro, 'investigadores': investigadores})
    
    return render(request, 'libros.html', {'libro': libro})
def eliminarLibros(request,id):
    libroEliminar = Libros.objects.get(id=id)
    libroEliminar.delete()
    messages.success(request,"libro ELIMINADO exitosamente")
    return redirect('inicio')