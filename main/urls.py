from django.urls import path
from . import views

#Plantilla para la pagina inicial. Deberia mostrar el index de views.py
urlpatterns = [
    path("", views.main, name="main"),

    path("login/", views.login, name="login"),

    path("logout/", exit, name="exit"),

    path("Agenda/", views.Agenda, name="agenda"),

    path("register/", views.register, name="register"),

    path("Agenda/config", views.config, name="config"),

    path("Agenda/info", views.info, name="info"),

    path("MiAgenda/config/historial", views.historial, name="historial"),

    path("test/", views.test, name="test"),
]