
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

from .forms import RegisterForm

from .models import Acciones, RegistroCO, Configuracion


# Create your views here.

def main(response):
    return HttpResponse("<h1>Presentación</h1>")

# All related to Login

def login_view(request):
    if request.method == 'post':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/Agenda') 
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def register(request):
    if request.method == "post":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/Login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def exit(response):
        logout(response)
        return redirect('')
from django.contrib import auth

def check_login(request):
    user = auth.get_user(request)
    if user.is_authenticated:
        print("User is logged in")
    else:
        login_view(request)


#All related to Agenda

@login_required
def Agenda(response):
    acciones = Acciones.objects.all()
    preferencia = Configuracion.objects.all()
    return render(response, "agenda/agenda.html",             
    {'acciones':acciones}
    )


def config(response):
    return HttpResponse("<h1>Configuracion<h1>")

def info(response):
    return render(response, "Information.html")

def historial(response):
    return HttpResponse("<h1>Historial<h1>")

def MiAgenda(response):
    return render(response, "Agenda.html")

def test(response):
    return HttpResponse("<h1>test</h1>")