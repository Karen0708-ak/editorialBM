from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio_libro'),
    path('nuevoLibro/', views.nuevoLibro, name='nuevoLibro'),
    path('guardarLibro/', views.guardarLibro, name='guardarLibro'),
    path('editarLibro/<int:id_libro>/', views.editarLibro, name='editarLibro'),
    path('actualizarLibro/<int:id_libro>/', views.actualizarLibro, name='actualizarLibro'),
    path('eliminarLibro/<int:id_libro>/', views.eliminarLibro, name='eliminarLibro'),
]