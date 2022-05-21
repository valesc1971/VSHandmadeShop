from cgi import print_directory
from datetime import datetime
from mailbox import NoSuchMailboxError
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail,EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
import string
from datetime import date
import datetime
import random


from .backend import MyBackend

from .models import  Usuario, Mensaje, Producto, Orden
from .forms import EmailForm, UsuarioForm, LoginForm, MensajeForm,  UserRegisterForm, ProductoForm, OrdenForm

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
            usuario.receive_newsletter=form.cleaned_data['receive_newsletter']
            usuario.save()
            messages.success(request, f"{usuario.nombre}, Gracias por registrarte con nosotros .")
        else:
            messages.error(request, 'rut no es valido' )
        return redirect('formulario_usuario')
    else:
        form = UsuarioForm()
        return render (request, 'aplicacion1/formulario_usuario.html',{"form":form})


def login(request):   #ingreso de usuario admin
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            usuario=form.cleaned_data["nombre"]
            clave=form.cleaned_data["password"]
            user=authenticate(request, username=usuario, password=clave)
            if user is not None:
                auth_login(request, user)
                messages.add_message(request, messages.INFO, f"Has ingresado como {usuario}." )
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
    messages.info(request, "Tu sesion ha terminado") 
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
                messages.info(request, "Gracias por tu mensaje. Me contactare a la brevedad") 
                html_content=render_to_string('aplicacion1/email_template.html')
                to_email = str(form['email'].value())
                msg = EmailMultiAlternatives('subject',html_content, 'valepython123@gmail.com',[to_email,])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                #send_mail('subject',body, 'valepython123@gmail.com',[to_email,],fail_silently = False )
        
              
                return redirect('/contacto')
        else:
            form = MensajeForm()
            return render (request, 'aplicacion1/contacto.html',{"form":form})

def mostrar_mensaje (request):  #muestra mensajes recibidos
    mensaje=Mensaje.objects.all()
    return render (request,'aplicacion1/mensajes.html',{"data":mensaje})

def editar_mensaje(request, id):  #formulario editar mensaje
        mensaje=Mensaje.objects.get(pk=id)
        form = MensajeForm(instance=mensaje)
        if request.method == "POST":
            form=MensajeForm(data=request.POST, instance=mensaje)
            form.save()
            return redirect('/mostrar_mensaje')
        else:
            return render (request, 'aplicacion1/editar_mensaje.html',{"form":form})

def eliminar_mensaje(request, id):
        mensaje=Mensaje.objects.get(pk=id)
        mensaje.delete()
        return redirect('/mensaje_mail')

def mensaje_mail(request,email):
    email_list = Mensaje.objects.filter(email=email)
    return render(request, 'aplicacion1/mensaje_mail.html', {"correo":email_list})
  

def page_not_found_view(request, exception): #mensaje de error
    return render(request, '404.html', status=404)

def productos_lista(request):
    producto=Producto.objects.all()
    return render (request,'aplicacion1/productos_lista.html',{"data":producto})

def  ingreso_productos(request):  # ingreso de nuevos productos
    form = ProductoForm()
    if request.method == "POST":
        form=ProductoForm(data=request.POST, files=request.FILES)
        producto=form.save (commit=False)
        producto.save()
        color=form.cleaned_data ['color']
        for col in color:
            producto.color.add(col)
        return redirect('productos_lista')

    else:
        return render (request, 'aplicacion1/ingreso_productos.html',{"form":form})

def producto_display(request):
    products=Producto.objects.all()
    return render (request,'aplicacion1/producto_display.html',{"products":products})

def compra_producto(request, id):
        orden=Producto.objects.get(pk=id)
        form = OrdenForm(initial={'email':request.user.email}, instance=orden)
        if request.method == "POST":
            form=OrdenForm(data=request.POST)
            form.save()
            messages.info(request, "Gracias por tu compra. Recibiras un email con tu numero de compra") 
            return redirect('/producto_display')
        else:
            return render (request, 'aplicacion1/compra_producto.html',{"form":form} )






