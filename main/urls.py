from django.urls import path
from . import views

#Plantilla para la pagina inicial. Deberia mostrar el index de views.py
urlpatterns = [
    path("", views.main, name="main"),
    path("v1/", views.v1, name="v1"),
    path("MiAgenda/", views.MiAgenda, name="MiAgenda"),
]