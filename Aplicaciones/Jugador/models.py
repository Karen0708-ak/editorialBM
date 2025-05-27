from django.db import models

# Create your models here.
class Jugador(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=200)
    celular = models.PositiveIntegerField()