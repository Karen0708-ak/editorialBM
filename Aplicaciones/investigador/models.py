from django.db import models


class Investigador(models.Model):
    id_investigador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
