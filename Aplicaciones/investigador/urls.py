from django.urls import path
from . import views
urlpatterns=[
    path('investigador',views.inicio,name='investigador'),
    path('nuevoInvestigador',views.nuevoInvestigador),
    path('guardarInvestigador',views.guardarInvestigador),
    path('eliminarInvestigador/<id_investigador>',views.eliminarInvestigador),
    path('editarInvestigador/<id_investigador>',views.editarInvestigador),
    path('procesarEdicionInvestigador',views.procesarEdicionInvestigador),
]