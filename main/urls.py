from django.urls import path, include
from .views import Cambiar_Verdad, Cambiar_Falso
from . import views
from .views import Agenda

#Plantilla para la pagina inicial. Deberia mostrar el index de views.py
urlpatterns = [
    path("", views.main, name="main"),

    path("", include('users.urls')),

    path("test/", views.test, name="test"),
    path("Agenda/", Agenda, name="agenda"),
    path("Agenda/info/", views.info, name="info"),
    path("Agenda/config/", views.config, name="config"),
    path("Agenda/config/historial", views.historial, name="historial"),

    path("Cambiar_Verdad/<int:id_accion>/", Cambiar_Verdad, name="Cambiar_Verdad"),
    path("Cambiar_Falso/<int:id_accion>/", Cambiar_Falso, name="Cambiar_Falso"),
    path("Valores/", views.Valores, name="Valores"),

    path("taylor/", views.Taylor, name="Taylor"),
]