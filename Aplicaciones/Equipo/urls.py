from django.urls import path
from . import views
urlpatterns=[
    path('inicioeq',views.inicio,name='inicioeq'),
    path('nuevoEquipo',views.nuevoEquipo),
    path('guardarEquipo',views.guardarEquipo),
    path('eliminarEquipo/<id_equipo>',views.eliminarEquipo),
    path('editarEquipo/<id_equipo>',views.editarEquipo),
    path('procesarEdicionEquipo',views.procesarEdicionEquipo),
]