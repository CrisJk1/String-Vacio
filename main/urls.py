from django.urls import path
from . import views

#Plantilla para la pagina inicial. Deberia mostrar el index de views.py
urlpatterns = [
    path("", views.main, name="main"),
    path("login/", views.v1, name="login"),
    path("login/MiAgenda/", views.MiAgenda, name="MiAgenda"),
    path("register/", views.register, name="register"),
    path("login/MiAgenda/config", views.config, name="config"),
    path("login/MiAgenda/info", views.info, name="info"),
    path("login/MiAgenda/config/historial", views.historial, name="historial"),
]