from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

# Create your views here.
#hola
def sign_in(request):

    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect ('Agenda/')
        
        form = LoginForm()
        return render(request, "login.html", {'form':form})
    
    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,password=password)
            if user:
                login(request, user)
                return redirect ('Agenda/')

        messages.error(request, '¡Nombre de usuario o contraseña no válidos!')
        return render(request, 'login.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request,'you been logged out')
    return redirect('/login')

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request,'register.html',{'form':form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/Agenda')
        else:
            messages.error(request, '¡Nombre de usuario o contraseña no válidos!')
            return render(request,'register.html',{'form':form})