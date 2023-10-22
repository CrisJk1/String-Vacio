
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


from .models import Acciones, RegistroCO

# Create your views here.

def main(response):
    return HttpResponse("<h1>Presentación</h1>")

# All related to Login

def login_view(request):
    if request.method == 'POST':
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

def exit(response):
        logout(response)
        return redirect('')

def register(response):
    return HttpResponse("<h1>Register<h1>")

#All related to Agenda

@login_required
def Agenda(response):
    acciones = Acciones.objects.all()
    return render(response, "agenda/agenda.html",             
    {'acciones':acciones}
    )


def config(response):
    return HttpResponse("<h1>Configuracion<h1>")

def info(response):
    return HttpResponse("<h1>Información<h1>")

def historial(response):
    return HttpResponse("<h1>Historial<h1>")

def test(response):
    return render(response, "Agenda.html")