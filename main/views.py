
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from datetime import date, timedelta


from .models import Acciones, RegistroCO, Configuracion


# Create your views here.

def main(response):
    return render(response, "Presentacion.html")

@login_required
def Agenda(response):
    #Creación de fila Usuario en tabla de configuracion (Base de datos)
    if Configuracion.objects.filter(Usuario = response.user.id).exists() == False:
        Configuracion.objects.create(Usuario= response.user)

    if response.user.is_authenticated:
        acciones = Acciones.objects.all()
        preferencias = Configuracion.objects.all()
        usuario = response.user
        for persona in preferencias:
            if persona.Usuario == usuario:
                elecciones = persona.Preferencias
        lista_elecciones = elecciones.split(',')
        del lista_elecciones[-1]
        acciones_preferidas = list()
        #Obtener id de las acciones
        id_acciones = []
        for identificador in acciones:
            id_acciones.append(identificador.pk)

        #Filtrar booleanos, obtener id de acciones con valor "True"
        valores = []
        i = 0
        for valor in lista_elecciones:
            if valor == "T":
                valores.append(id_acciones[i])
                i+=1
            else:
                i+=1
        for accion in acciones:
            if accion.pk in valores:
                acciones_preferidas.append(accion)

        #Sacar datos de carbono
        for persona in preferencias:
            if persona.Usuario == usuario:
                deuda = int(persona.Deuda)
        
        #Boss Fight
        boton_activador = False
        if deuda == 0:
            boton_activador = True

        return render(response, "Agenda.html",             
        {'acciones':acciones_preferidas,
        'prefencias':lista_elecciones,
        'deuda':deuda,
        'activador': boton_activador,
        })
    else:
        messages.error(response, 'Debes iniciar sesion antes de continuar')
        return redirect('/login')

@login_required
def config(response):
    usuario = response.user
    config = Configuracion.objects.all()
    acciones = Acciones.objects.all()
    lista_valores = []
    i= 0

    #Creación de fila Usuario en tabla de configuracion (Base de datos)
    if Configuracion.objects.filter(Usuario = response.user.id).exists() == False:
        Configuracion.objects.create(Usuario= response.user)

    #Verificar identidad de persona y obtener string con preferencias
    for persona in config:
        if persona.Usuario == usuario:
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
    del elecciones[-1]

    #Obtener id de las acciones
    id_acciones = []
    for identificador in acciones:
        id_acciones.append(identificador.pk)

    #Filtrar booleanos, obtener id de acciones con valor "True"
    for valor in elecciones:
        if valor == "T":
            lista_valores.append(id_acciones[i])
            i+=1
        else:
            i+=1
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
    #Obtener id de las acciones
    id_acciones = []
    for identificador in acciones:
        id_acciones.append(identificador.pk)
    posicion = id_acciones.index(id_accion)

    Prefer = Prefer.split(",")
    Prefer[posicion] = "T"
    linea_valores = ''
    for valor in Prefer:
        if len(linea_valores) < ((len(acciones)*2)-1):
            linea_valores += valor+","
        elif len(linea_valores) == ((len(acciones)*2)-1):
            linea_valores += valor
    Configuracion.objects.filter(Usuario = request.user.id).update(Preferencias = linea_valores)
    return redirect('/Agenda/config')

def Cambiar_Falso(request, id_accion):
    #Funcion para cambiar el valor de T a F en la base de datos
    usuario = request.user
    acciones = Acciones.objects.all()
    Ajustes = Configuracion.objects.all()
    for persona in Ajustes:
        if persona.Usuario == usuario:
            Prefer = persona.Preferencias
    #Obtener id de las acciones
    id_acciones = []
    for identificador in acciones:
        id_acciones.append(identificador.pk)
    posicion = id_acciones.index(id_accion)

    Prefer = Prefer.split(",")
    Prefer[posicion] = "F"
    linea_valores = ''
    for valor in Prefer:
        if len(linea_valores) < ((len(acciones)*2)-1):
            linea_valores += valor+","
        elif len(linea_valores) == ((len(acciones)*2)-1):
            linea_valores += valor
    Configuracion.objects.filter(Usuario = request.user.id).update(Preferencias = linea_valores)
    return redirect('/Agenda/config')

@csrf_exempt
def Valores(request):
    acciones = Acciones.objects.all()
    ajuste = Configuracion.objects.all()
    suma = 0

    if request.method == 'POST':
        for acc in acciones:
            if request.POST.get(acc.Accion):
                if acc.Acumulable == True:
                    calculo = float(request.POST.get(acc.Accion))*float(acc.Huella)
                    suma += calculo
                else:
                    suma += float(request.POST.get(acc.Accion))
    for persona in ajuste:
        if persona.Usuario == request.user:
            cantidad = persona.Deuda
    ahorro = float(cantidad)-suma
    #Si el carbono llega hasta 0, se detiene ahí, no se va a negativos, ni se agrega al historial un ahorro
    if ahorro <= 0:
        ahorro = 0
    Configuracion.objects.filter(Usuario = request.user.id).update(Deuda = ahorro)
    if RegistroCO.objects.filter(Usuario = request.user.id, Fecha = date.today()).exists() == False:
        RegistroCO.objects.create(Usuario= request.user, Fecha = date.today(), Repositorio = suma)
    else:
        visitante = RegistroCO.objects.get(Usuario= request.user, Fecha = date.today())
        if ahorro != 0:
            valor_definitivo = float(visitante.Repositorio)
            valor_definitivo += suma
            RegistroCO.objects.filter(Usuario= request.user, Fecha = date.today()).update(Repositorio = valor_definitivo)

    
    return redirect('/Agenda/')

def info(response):
    return render(response, "Information.html")

@login_required
def historial(response):
    registro = RegistroCO.objects.all()
    idi = response.user
    existencia = RegistroCO.objects.filter(Usuario = response.user.id).exists()
    lista_años = []
    for elementos in registro:
        if elementos.Usuario == idi:
            if elementos.Fecha.year not in lista_años:
                lista_años.append(elementos.Fecha.year)
    lista_años.sort()
    return render(response, "Historial.html", {
        'registro': registro,
        'usuario': idi,
        'existencia': str(existencia),
        'orden': lista_años,
    })

def test(response):
    return HttpResponse("<h1>test</h1>")

def Taylor(response):
    Configuracion.objects.filter(Usuario = response.user.id).update(Deuda = 4400.00)
    print("aaaaa")
    return render(response, "Taylor.html")

