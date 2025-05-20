from django.urls import path
from . import views
urlpatterns=[
    path('inicioau',views.inicio,name='inicioau'),
    path('nuevoAutor',views.nuevoAutor),
    path('guardarAutor',views.guardarAutor),
    path('eliminarAutor/<id_autor>',views.eliminarAutor),
    path('editarAutor/<id_autor>',views.editarAutor),
    path('procesarEdicionAutor',views.procesarEdicionAutor),
]