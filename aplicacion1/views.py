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
def usuarios(request):  # listado de usuarios del sitio
    usuario=Usuario.objects.all()
    return render (request,'aplicacion1/usuarios.html',{"data":usuario})

def ejemplo(request):  # ejemplo de plantilla / solo para ensayo
    return render (request,'aplicacion1/ejemplo.html')


def  formulario_usuario(request):  # registro de usuario

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

def login_externo(request):         #login usuario para desarrollar mas adelante
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

def bienvenido_externo (request): # no usuado actualmente
    return render (request, 'aplicacion1/bienvenido_externo.html')

def salir_externo (request): #no usado actualmente
    logout (request)
    return redirect ("/login_externo")

def login(request):   #ingreso de usuario admin
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
def bienvenido (request):  #mensaje de bienvenida usaurio admin
    return render (request, 'aplicacion1/bienvenido.html')

def salir (request):  #salir usuario admin
    logout (request)
    messages.info(request, "You have successfully logged out.") 
    return redirect ("/login")

def register(request):  #registro usuario admin
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


def contacto(request):  #formulario contacto para envia mensajes q se almacenan en objecto mensajes
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
def mostrar_mensaje (request):  #muestra mensajes recibidos
    mensaje=Mensaje.objects.all()
    return render (request,'aplicacion1/mensajes.html',{"data":mensaje})


def page_not_found_view(request, exception): #mensaje de error
    return render(request, '404.html', status=404)

<<<<<<< HEAD
def productos(request):
    producto=Producto.objects.all()
    return render (request,'aplicacion1/productos.html',{"data":producto})
=======

""" registro / ingreso/ clientes externos..para desarrollo porsterior
def registro_cliente(request):
    cliente=Cliente.objects.all()
    return render (request,'aplicacion1/registro_cliente.html',{"data":cliente})

def  formulario_cliente(request):

    form = ClienteForm()
    
    if request.method == "POST":
        form=ClienteForm(data=request.POST)

        if form.is_valid():
            cliente=Cliente()
            cliente.nombre=form.cleaned_data['nombre']
            cliente.clave=form.cleaned_data['clave']
            cliente.save()

        return redirect('bienvenido_externo')
    else:
        form = ClienteForm()
        return render (request, 'aplicacion1/formulario_cliente.html',{"form":form})

def login_cliente(request):
    if request.method == "POST":
        form = LoginExtForm(data = request.POST)
        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            clave=form.cleaned_data["clave"]
            user=MyBackend2.authenticate(request, username=nombre, password=clave)
            if user is not None:

                auth_login(request, user)
            return render (request, 'bienvenido_cliente', {'user':user})
    else:
        form= LoginExtForm()
        return render (request, 'aplicacion1/login_cliente.html', {"form":form})

def bienvenido_cliente (request):
    return render (request, 'aplicacion1/bienvenido_cliente.html')

def salir_cliente (request):
    logout (request)
    return redirect ("/login_cliente")


def clientes(request):
    usuario=Cliente.objects.all()
    return render (request,'aplicacion1/clientes.html',{"data":usuario})

"""
>>>>>>> 41a720e110324483b7bfcea52a0d3f4c92f7c074
