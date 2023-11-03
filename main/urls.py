from django.urls import path, include
from .views import Cambiar_Verdad, Cambiar_Falso
from . import views

#Plantilla para la pagina inicial. Deberia mostrar el index de views.py
urlpatterns = [
    path("", views.main, name="main"),

    path("", include('users.urls')),

    path("test/", views.test, name="test"),
    path("Agenda/", views.Agenda, name="agenda"),
    path("MiAgenda/config", views.config, name="config"),
    path("Cambiar_Verdad/<int:id_accion>/", Cambiar_Verdad, name="Cambiar_Verdad"),
    path("Cambiar_Falso/<int:id_accion>/", Cambiar_Falso, name="Cambiar_Falso"),
    path("MiAgenda/config/historial", views.historial, name="historial"),

    path("MiAgenda/", views.MiAgenda, name="MiAgenda"),
    path("/", views.info, name="info"),
]