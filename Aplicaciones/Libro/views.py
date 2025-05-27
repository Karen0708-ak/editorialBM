from .models import Autor
from .models import Libro
from .models import Libreria
from django.shortcuts import render, redirect
from django.contrib import messages
def inicio(request):
    listadoLibro=Libro.objects.all()
    return render(request,"iniciolib.html",{'libro':listadoLibro})

def nuevoLibro(request):
    rautor=Autor.objects.all()
    rlibreria=Libreria.objects.all()
    return render(request,"nuevoLibro.html",{'autor':rautor,'libreria':rlibreria})
#Almacenando los datos de cargo en la Bdd
def guardarLibro(request):
    isbn = request.POST["isbn"]
    titulo = request.POST["titulo"]
    anio = request.POST["anio"]
    autorid = request.POST["autor"]
    autor=Autor.objects.get(id_autor=autorid)
    libreriaid = request.POST["libreria"]
    libreria=Libreria.objects.get(id_libreria=libreriaid)
    nuevoLibro=Libro.objects.create(
            isbn=isbn,
            titulo=titulo,
            anio=anio,
            autor=autor,
            libreria=libreria,
        )
    #mensaje de confirmacion
    messages.success(request,"Libreria guardado exitosamente")
    return redirect('iniciolib')

def eliminarLibro(request,id_libro):
    libroEliminar = Libro.objects.get(id_libro=id_libro)
    libroEliminar.delete()
    messages.success(request,"Libro ELIMINADO exitosamente")
    return redirect('iniciolib')

#editar
def editarLibro(request,id_libro):
    libroEditar=Libro.objects.get(id_libro=id_libro)
    rautor=Autor.objects.all()
    rlibreria=Libreria.objects.all()
    return render(request,"editarLibro.html",{'libroEditar':libroEditar, 'autor':rautor,'libreria':rlibreria})

def procesarEdicionLibro(request):
    id_libro=request.POST["id_libro"]
    isbn = request.POST["isbn"]
    titulo = request.POST["titulo"]
    anio = request.POST["anio"]
    autorid = request.POST["autor"]
    autor=Autor.objects.get(id_autor=autorid)
    libreriaid = request.POST["libreria"]
    libreria=Libreria.objects.get(id_libreria=libreriaid)
    libro=Libro.objects.get(id_libro=id_libro)
    libro.isbn=isbn
    libro.titulo=titulo
    libro.anio= anio
    libro.autor= autor
    libro.libreria= libreria
    libro.save()
    #mensaje de confirmacion
    messages.success(request,"Libro ACTUALIZADO exitosamente")
    return redirect('iniciolib')