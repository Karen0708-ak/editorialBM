from django.urls import path
from . import views
urlpatterns=[
    path('iniciolib/',views.inicio,name='iniciolib'),
    path('nuevoLibro/',views.nuevoLibro),
    path('guardarLibro/',views.guardarLibro),
    path('eliminarLibro/<id_libro>',views.eliminarLibro),
    path('editarLibro/<id_libro>',views.editarLibro),
    path('procesarEdicionLibro/',views.procesarEdicionLibro),
]