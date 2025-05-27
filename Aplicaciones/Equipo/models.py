from django.db import models
# Importamos modelos 
from Aplicaciones.Jugador.models import Jugador

class Equipo (models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    partidos_ganados = models.PositiveIntegerField()
    partidos_perdidos = models.PositiveIntegerField()
    jugador = models.ManyToManyField(Jugador)