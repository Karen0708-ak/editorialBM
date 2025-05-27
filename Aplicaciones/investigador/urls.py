from django.urls import path
from . import views

urlpatterns = [
    path('investigador/', views.inicio, name='investigador'),
    path('nuevoInvestigador/', views.nuevoInvestigador, name='nuevoInvestigador'),
    path('guardarInvestigador/', views.guardarInvestigador, name='guardarInvestigador'),  # <-- Agregado name
    path('eliminarInvestigador/<id_investigador>', views.eliminarInvestigador, name='eliminarInvestigador'),  # <-- Agregado name
    path('editarInvestigador/<id_investigador>', views.editarInvestigador, name='editarInvestigador'),  # <-- Agregado name
    path('procesarEdicionInvestigador', views.procesarEdicionInvestigador),
]