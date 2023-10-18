from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def main(response):
    return HttpResponse("<h1>Presentación</h1>")

def Agenda(response):
    return render(response, "agenda.html")

def login(response):
    return HttpResponse("<h1>Login</h1>")

def register(response):
    return HttpResponse("<h1>Register<h1>")

def config(response):
    return HttpResponse("<h1>Configuracion<h1>")

def info(response):
    return HttpResponse("<h1>Información<h1>")

def historial(response):
    return HttpResponse("<h1>Historial<h1>")

def test(response):
    return render(response, "Agenda.html")