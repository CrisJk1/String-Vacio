from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def main(response):
    return HttpResponse("<h1>Pagina principal</h1>")

def v1(response):
    return HttpResponse("<h1>Login</h1>")

def MiAgenda(response):
    return render(response, "MiAgenda.html")