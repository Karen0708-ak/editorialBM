from django.urls import path
from .import views

urlpatterns = [
    path('', views.inicio, name='inicioLibro'),
    path('nuevoLibro/', views.nuevoLibro, name='nuevoLibro'),
    path('guardarLibro/', views.guardarLibro, name='guardarLibro'),
    path('eliminarLibro/<int:id>/', views.eliminarLibro, name='eliminarLibro'),
]
