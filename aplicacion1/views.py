from cgi import print_directory
from mailbox import NoSuchMailboxError
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .backend import MyBackend

from .models import Usuario, Mensaje, Producto
from .forms import UsuarioForm, LoginForm, MensajeForm, LoginExtForm, UserRegisterForm

MyBackend=MyBackend()

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
            usuario.clave=form.cleaned_data['clave']
            usuario.save()

        return redirect('bienvenido_externo')
    else:
        form = UsuarioForm()
        return render (request, 'aplicacion1/formulario_usuario.html',{"form":form})

def login_externo(request):
    if request.method == "POST":
        form = LoginExtForm(data = request.POST)
        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            clave=form.cleaned_data["clave"]
            user=MyBackend.authenticate(request, username=nombre, password=clave)
            if user is not None:
                auth_login(request, user)
            return render (request, 'bienvenido_externo', {'user':user})
    else:
        form= LoginExtForm()
        return render (request, 'aplicacion1/login_externo.html', {"form":form})

def bienvenido_externo (request):
    return render (request, 'aplicacion1/bienvenido_externo.html')

def salir_externo (request):
    logout (request)
    return redirect ("/login_externo")

def login(request):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            usuario=form.cleaned_data["nombre"]
            clave=form.cleaned_data["password"]
            user=authenticate(request, username=usuario, password=clave)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"Has ingresado como {usuario}.")
                return redirect ('bienvenido')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form= LoginForm()
    return render (request, 'aplicacion1/login.html', {"form":form})

@login_required (login_url="/login")
def bienvenido (request):
    return render (request, 'aplicacion1/bienvenido.html')

def salir (request):
    logout (request)
    messages.info(request, "You have successfully logged out.") 
    return redirect ("/login")

def register(request):
    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente.')
            return redirect ('login')
    
    else:
        form=UserRegisterForm()

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

def productos(request):
    producto=Producto.objects.all()
    return render (request,'aplicacion1/productos.html',{"data":producto})