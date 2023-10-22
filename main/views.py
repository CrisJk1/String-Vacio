from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def main(response):
    return HttpResponse("<h1>Presentación</h1>")

@login_required
def Agenda(response):
    return render(response, "agenda.html")


def login(response):
    return render(response, "registration/login.html") 

def exit(response):
        logout(response)
        return redirect('')


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