from django.db import models
from Aplicaciones.investigador.models import Investigador

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    anio = models.CharField(max_length=4)
    ISBN = models.CharField(max_length=20, unique=True)
    paginas = models.CharField(max_length=4)
    investigadores = models.ManyToManyField(Investigador, related_name='libros')

    def __str__(self):
        return self.titulo