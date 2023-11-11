
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User


from .models import Acciones, RegistroCO, Configuracion


# Create your views here.

def main(response):
    return HttpResponse("<h1>Presentación</h1>")


def Agenda(response):
    if not response.user.is_authenticated:
        messages.error(response, 'Debes iniciar sesion antes de continuar')
        response = redirect('/login')
        return response
    else:
        acciones = Acciones.objects.all()
        preferencias = Configuracion.objects.all()
        usuario = response.user
        for persona in preferencias:
            if persona.Usuario == usuario:
                elecciones = persona.Preferencias
        lista_elecciones = elecciones.split(',')
        del lista_elecciones[-1]
        print(lista_elecciones)
        for accion in acciones:
            id = int(accion.pk)-14
            acciones_preferidas = list()
            if lista_elecciones[id] == 'T':
                acciones_preferidas.append(accion)
        return render(response, "Agenda.html",             
        {'acciones':acciones_preferidas,
         'prefencias':lista_elecciones}
    )


def config(response):
    usuario = response.user
    config = Configuracion.objects.all()
    acciones = Acciones.objects.all()
    lista_valores = []
    encontrar = False
    i= 0
    
    #Verificar identidad de persona y obtener string con preferencias
    for persona in config:
        if persona.Usuario == usuario:
            elecciones = persona.Preferencias
            encontrar = True
    if encontrar == False:
        Configuracion.objects.create(Usuario= response.user)
        elecciones = persona.Preferencias

    #Creacion de preferencias (Todas Falsas como default)
    if elecciones == None or len(elecciones) < ((len(acciones)*2)-1):
        elecciones = ""
        while len(elecciones)<((len(acciones)*2)-1):
            elecciones += "F"
            if len(elecciones)<((len(acciones)*2)-1):
                elecciones += ","
    Configuracion.objects.filter(Usuario = response.user.id).update(Preferencias = elecciones)
    elecciones = elecciones.split(",")

    #Obtener id menor en tabla de datos (Para que a todos nos funcione la base de datos)
    id_inicial = 100
    for identificador in acciones:
        id_acc = identificador.pk
        if id_acc < id_inicial:
            id_inicial = id_acc
    #Filtrar booleanos, obtener id de acciones con valor "True"
    for valor in elecciones:
        if valor == "T":
            lista_valores.append(i+id_inicial)
            i+=1
        else:
            i+=1
    print(lista_valores)
    return render(response, "Config.html", {
        'Acciones': acciones,
        'Valores': lista_valores
    })

def Cambiar_Verdad(request, id_accion):
    #Funcion para cambiar el valor de F a T en la base de datos
    usuario = request.user
    acciones = Acciones.objects.all()
    Ajustes = Configuracion.objects.all()
    for persona in Ajustes:
        if persona.Usuario == usuario:
            Prefer = persona.Preferencias
    posicion = int(id_accion)-14
    Prefer = Prefer.split(",")
    Prefer[posicion] = "T"
    linea_valores = ''
    for valor in Prefer:
        if len(linea_valores) < ((len(acciones)*2)-1):
            linea_valores += valor+","
        elif len(linea_valores) == ((len(acciones)*2)-1):
            linea_valores += valor
    Configuracion.objects.filter(Usuario = request.user.id).update(Preferencias = linea_valores)
    return redirect('/MiAgenda/config')

def Cambiar_Falso(request, id_accion):
    #Funcion para cambiar el valor de T a F en la base de datos
    usuario = request.user
    acciones = Acciones.objects.all()
    Ajustes = Configuracion.objects.all()
    for persona in Ajustes:
        if persona.Usuario == usuario:
            Prefer = persona.Preferencias
    posicion = int(id_accion)-14
    Prefer = Prefer.split(",")
    Prefer[posicion] = "F"
    linea_valores = ''
    for valor in Prefer:
        if len(linea_valores) < ((len(acciones)*2)-1):
            linea_valores += valor+","
        elif len(linea_valores) == ((len(acciones)*2)-1):
            linea_valores += valor
    Configuracion.objects.filter(Usuario = request.user.id).update(Preferencias = linea_valores)
    return redirect('/MiAgenda/config')

def info(response):
    return render(response, "Information.html")

def historial(response):
    return HttpResponse("<h1>Historial<h1>")

@login_required
def MiAgenda(response):
    return render(response, "Agenda.html")

def test(response):
    return HttpResponse("<h1>test</h1>")

