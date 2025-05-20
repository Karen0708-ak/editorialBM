from django.db import models

# Importamos modelos de otras apps
from Aplicaciones.Autor.models import Autor
from Aplicaciones.Libreria.models import Libreria

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=20, unique=True)
    titulo = models.CharField(max_length=200)
    anio = models.PositiveIntegerField()

    # Relación muchos a muchos con autores
    autores = models.ManyToManyField(Autor, related_name='libros')

    # Relación muchos a muchos con librerías
    librerias = models.ManyToManyField(Libreria, related_name='libros')

