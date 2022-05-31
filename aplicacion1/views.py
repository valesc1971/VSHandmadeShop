from cgi import print_directory
from datetime import datetime
from mailbox import NoSuchMailboxError
from django.shortcuts import redirect, render, get_object_or_404
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
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .backend import MyBackend

from .models import  Usuario, Mensaje, Producto, Orden, Order, OrderItem
from .forms import EmailForm, UsuarioForm, LoginForm, MensajeForm,  UserRegisterForm, ProductoForm, OrdenForm, CheckoutForm

import xlwt

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
        messages.info(request, 'eliminado correctamente')
        return redirect('/mostrar_mensaje')

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

def editar_producto(request, id):  #formulario editar mensaje
        producto=Producto.objects.get(pk=id)
        form = ProductoForm(instance=producto)
        if request.method == "POST":
            form=ProductoForm(data=request.POST, instance=producto,files=request.FILES)
            producto=form.save (commit=False)
            producto.save()
            color=form.cleaned_data ['color']
            for col in color:
                producto.color.add(col)
            return redirect('productos_lista')

        else:
            return render (request, 'aplicacion1/editar_producto.html',{"form":form})

def eliminar_producto(request, id):
        producto=Producto.objects.get(pk=id)
        producto.delete()
        return redirect('/productos_lista')

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

def compra_user(request,user):
    compra_user = Order.objects.filter(user=user)
    print(compra_user)
    return render(request, 'aplicacion1/compra_user.html', {"compra_user":compra_user})

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'aplicacion1/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "No tiene ordenes pendientes")
            return redirect("/")

class ItemDetailView(DetailView):
    model = Producto
    template_name = "aplicacion1/product.html"

def add_to_cart(request, slug):
    item = get_object_or_404(Producto, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Cantidad actualizada")
            return redirect("order_summary")
        else:
            order.items.add(order_item)
            messages.info(request, "Se agrego este producto a tu orden")
            return redirect("order_summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Se agrego este producto a tu orden.")
        return redirect("order_summary")

def remove_from_cart(request, slug):
    item = get_object_or_404(Producto, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "El producto ha sido eliminido de su orden.")
            return redirect("order_summary")
        else:
            messages.info(request, "Este producto no estaba en tu carro")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "No tienes una orden pendiente")
        return redirect("product", slug=slug)

def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Producto, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "Se actualizo la cantidad de este producto.")
            return redirect("order_summary")
        else:
            messages.info(request, "Este producto no esta en tu carro")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "No tienes una orden pendiente")
        return redirect("product", slug=slug)

class CheckoutView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        context = {'order': order,}
        return render(self.request, "aplicacion1/checkout.html", context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        order = Order.objects.get(user=self.request.user, ordered=False)
        order.ordered=True
        order.ref_code = create_ref_code()
        order.save()
        messages.success(self.request, "Se ha procesado tu orden. Gracias!")
        #html_content=render_to_string('aplicacion1/email_template.html')
        text_content =f'{order.user.email} tu numero de orden es:  {order.ref_code}'
        to_email = str(order.user.email)
        msg = EmailMultiAlternatives('Gracias por tu compra',text_content, 'valepython123@gmail.com',[to_email,])
        #msg.attach_alternative(html_content, "text/html")
        msg.send()
        return redirect("/")

def export_excel (request):
    response= HttpResponse(content_type='application/vnd.ms-excel')
    response['Content_Disposition'] = 'attachment; filename=Listado.xlsx'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('ListadoProductos')
    
    row_num = 0 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    columns = ['Nombre', 'Descripcion', 'Precio']
    for col_num in range (len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()

    rows=Producto.objects.all().values_list('nombre', 'descripcion', 'precio')
    for row in rows:
        row_num+=1
        for col_num in range (len(row)):
            ws.write(row_num, col_num, row[col_num], font_style )
    
    wb.save(response)
    return response


