from django.db import models
# Importamos modelos 
from Aplicaciones.Autor.models import Autor
from Aplicaciones.Libreria.models import Libreria

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=20, unique=True)
    titulo = models.CharField(max_length=200)
    anio = models.PositiveIntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    libreria = models.ForeignKey(Libreria, on_delete=models.CASCADE)