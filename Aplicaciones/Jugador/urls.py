from django.urls import path
from . import views
urlpatterns=[
    path('inicioju',views.inicio,name='inicioju'),
    path('nuevoJugador',views.nuevoJugador),
    path('guardarJugador',views.guardarJugador),
    path('eliminarJugador/<id_jugador>',views.eliminarJugador),
    path('editarJugador/<id_jugador>',views.editarJugador),
    path('procesarEdicionJugador',views.procesarEdicionJugador),
]