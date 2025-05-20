from django.urls import path
from . import views
urlpatterns=[
    path('inicioau',views.inicio,name='inicioau'),
]