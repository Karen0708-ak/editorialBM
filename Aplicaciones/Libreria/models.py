from django.db import models
class Libreria(models.Model):
    id_libreria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True)