
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

from .models import Acciones, RegistroCO, Configuracion


# Create your views here.

def main(response):
    return HttpResponse("<h1>Presentación</h1>")

@login_required
def Agenda(response):
    acciones = Acciones.objects.all()
    preferencia = Configuracion.objects.all()
    return render(response, "agenda/agenda.html",             
    {'acciones':acciones}
    )


def config(response):
    config = Configuracion.objects.all()
    acciones = Acciones.objects.all()
    return render(response, "Config.html", {
        'Acciones': acciones
    })

def info(response):
    return render(response, "Information.html")

def historial(response):
    return HttpResponse("<h1>Historial<h1>")

def MiAgenda(response):
    return render(response, "Agenda.html")

def test(response):
    return HttpResponse("<h1>test</h1>")