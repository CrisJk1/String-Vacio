from django.urls import path, include
from . import views

#Plantilla para la pagina inicial. Deberia mostrar el index de views.py
urlpatterns = [
    path("", views.main, name="main"),

    path("", include('users.urls')),

    path("test/", views.test, name="test"),
    path("Agenda/", views.Agenda, name="agenda"),
    path("MiAgenda/config", views.config, name="config"),
    path("MiAgenda/config/historial", views.historial, name="historial"),

    path("MiAgenda/", views.MiAgenda, name="MiAgenda"),
    path("/", views.info, name="info"),
    path("/TyC", views.TyC, name="TyC"),
]