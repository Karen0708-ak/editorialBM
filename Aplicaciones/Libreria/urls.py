from django.urls import path
from . import views
urlpatterns=[
    path('inicioli',views.inicio,name='inicioli'),
    path('nuevaLibreria',views.nuevaLibreria),
    path('guardarLibreria',views.guardarLibreria),
    path('eliminarLibreria/<id_libreria>',views.eliminarLibreria),
    path('editarLibreria/<id_libreria>',views.editarLibreria),
    path('procesarEdicionLibreria',views.procesarEdicionLibreria),
]