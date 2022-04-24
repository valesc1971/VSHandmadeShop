from mailbox import NoSuchMailboxError
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario, Mensaje
from .forms import UsuarioForm, LoginForm, MensajeForm


# Create your views here.

def index(request):
    return render (request,'aplicacion1/index.html')


def productos(request):
    return render (request,'aplicacion1/productos.html')

@login_required
def usuarios(request):
    usuario=Usuario.objects.all()
    return render (request,'aplicacion1/usuarios.html',{"data":usuario})

def ejemplo(request):
    return render (request,'aplicacion1/ejemplo.html')

@login_required
def  formulario_usuario(request):

    form = UsuarioForm()
    
    if request.method == "POST":
        form=UsuarioForm(data=request.POST)

        if form.is_valid():
            usuario=Usuario()
            usuario.rut=form.cleaned_data['rut']
            usuario.nombre=form.cleaned_data['nombre']
            usuario.apellido=form.cleaned_data['apellido']
            usuario.edad=form.cleaned_data['edad']
            usuario.email=form.cleaned_data['email']
            usuario.save()

        return redirect('/usuarios')
    else:
        form = UsuarioForm()
        return render (request, 'aplicacion1/formulario_usuario.html',{"form":form})

def login(request):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            usuario=form.cleaned_data["nombre"]
            clave=form.cleaned_data["password"]
            user=authenticate(request, username=usuario, password=clave)
            if user is not None:
                auth_login(request, user)
            return redirect ('bienvenido')
    else:
        form= LoginForm()
        return render (request, 'aplicacion1/login.html', {"form":form})

@login_required (login_url="/login")
def bienvenido (request):
    return render (request, 'aplicacion1/bienvenido.html')

def salir (request):
    logout (request)
    return redirect ("/login")

def register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente.')
    
    else:
        form=UserCreationForm()

    context = {'form':form}

    return render (request, 'aplicacion1/register.html', context)


def contacto(request):
        form = MensajeForm()
        if request.method == "POST":
            form=MensajeForm(data=request.POST)

            if form.is_valid():
                message=Mensaje()
                message.nombre=form.cleaned_data['nombre']
                message.apellido=form.cleaned_data['apellido']
                message.email=form.cleaned_data['email']
                message.mensaje=form.cleaned_data['mensaje']
                message.save()

            return redirect('/contacto')
        else:
            form = MensajeForm()
            return render (request, 'aplicacion1/contacto.html',{"form":form})



@login_required
def mostrar_mensaje (request):
    mensaje=Mensaje.objects.all()
    return render (request,'aplicacion1/mensajes.html',{"data":mensaje})


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
