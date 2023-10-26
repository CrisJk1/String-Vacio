from django.urls import path
from . import views

#Plantilla para la pagina inicial. Deberia mostrar el index de views.py
urlpatterns = [
    path("", views.main, name="main"),

    path("login/", views.login_view, name="login_view"),
    path("logout/", exit, name="exit"),
    path("register/", views.register, name="register"),
    path("test/", views.test, name="test"),
    path("Agenda/", views.Agenda, name="agenda"),
    path("MiAgenda/config", views.config, name="config"),
    path("MiAgenda/config/historial", views.historial, name="historial"),

    path("MiAgenda/", views.MiAgenda, name="MiAgenda"),
    path("/", views.info, name="info"),
]