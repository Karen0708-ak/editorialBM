from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from Aplicaciones.Autor.models import Autor
from Aplicaciones.Libreria.models import Libreria
from django.contrib import messages

def inicio(request):
    libros = Libro.objects.all()
    return render(request, "iniciobo.html", {'libros': libros})

def nuevoLibro(request):
    autores = Autor.objects.all()
    librerias = Libreria.objects.all()
    return render(request, "agregarLibro.html", {
        'autores': autores,
        'librerias': librerias
    })

def guardarLibro(request):
    if request.method == 'POST':
        try:
            libro = Libro(
                isbn=request.POST.get('isbn'),
                titulo=request.POST.get('titulo'),
                anio=request.POST.get('anio')
            )
            libro.save()
            
            autores_ids = request.POST.getlist('autores')
            librerias_ids = request.POST.getlist('librerias')
            
            libro.autores.set(autores_ids)
            libro.librerias.set(librerias_ids)
            
            messages.success(request, 'Libro agregado correctamente')
        except Exception as e:
            messages.error(request, f'Error al agregar libro: {str(e)}')
    
    return redirect('inicio_libro')

def editarLibro(request, id_libro):
    libro = get_object_or_404(Libro, id_libro=id_libro)
    autores = Autor.objects.all()
    librerias = Libreria.objects.all()
    
    autores_seleccionados = [autor.id for autor in libro.autores.all()]
    librerias_seleccionadas = [libreria.id for libreria in libro.librerias.all()]
    
    return render(request, "editarLibro.html", {
        'libro': libro,
        'autores': autores,
        'librerias': librerias,
        'autores_seleccionados': autores_seleccionados,
        'librerias_seleccionadas': librerias_seleccionadas
    })

def actualizarLibro(request, id_libro):
    if request.method == 'POST':
        try:
            libro = Libro.objects.get(id_libro=id_libro)
            libro.isbn = request.POST.get('isbn')
            libro.titulo = request.POST.get('titulo')
            libro.anio = request.POST.get('anio')
            libro.save()
            
            autores_ids = request.POST.getlist('autores')
            librerias_ids = request.POST.getlist('librerias')
            
            libro.autores.set(autores_ids)
            libro.librerias.set(librerias_ids)
            
            messages.success(request, 'Libro actualizado correctamente')
        except Exception as e:
            messages.error(request, f'Error al actualizar libro: {str(e)}')
    
    return redirect('inicio_libro')

def eliminarLibro(request, id_libro):
    libro = get_object_or_404(Libro, id_libro=id_libro)
    try:
        libro.delete()
        messages.success(request, 'Libro eliminado correctamente')
    except Exception as e:
        messages.error(request, f'Error al eliminar libro: {str(e)}')
    return redirect('inicio_libro')