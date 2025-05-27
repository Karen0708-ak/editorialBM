from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('nuevosLibros/', views.nuevosLibros, name='nuevosLibros'),
    path('guardarLibros/', views.guardarLibros, name='guardarLibros'),
    path('editarLibros/<int:id>/', views.editarLibros, name='editarLibros'),
    path('eliminarLibros/<int:id>/', views.eliminarLibros, name='eliminarLibros'),
]