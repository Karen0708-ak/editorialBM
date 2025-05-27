from django.db import models

from Aplicaciones.investigador.models import Investigador

class Libros(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    anio = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=100)
    paginas = models.CharField(max_length=100)

    investigador = models.ManyToManyField(Investigador, related_name='libro')