from django.contrib.auth.models import AbstractUser, User
from django.db import models
from PIL import Image
from django.shortcuts import reverse
from django.conf import settings
# Create your models here.

class Usuario(models.Model):
    rut=models.CharField(max_length=15, null=False)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=100, null=False)
    edad=models.IntegerField()
    email=models.EmailField()
    receive_newsletter = models.BooleanField( blank=True)

    def __str__(self):
        return self.nombre

class Mensaje(models.Model):
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=100, null=False)
    email=models.EmailField()
    mensaje=models.TextField(max_length=500, null=False)

class Clasificacion (models.Model): #1 categoria puede estar asociado a varios productos, pero 1 producto solo 1 categoria (1 a n)
      nombre= models.CharField(max_length=50)

      def __str__(self):
          return self.nombre

class Codigo (models.Model): # 1 codigo asociado a 1 solo prod y un prod solo 1 codigo
    codigo = models.CharField(max_length=50)

    def __str__(self):
          return self.codigo

class Color (models.Model): # 1 producto puede tener muchos colores y un color puede ser para muchos prods
    color = models.CharField(max_length=50)

    def __str__(self):
          return self.color


class Producto(models.Model):
    nombre=models.CharField(max_length=50, null=False)
    descripcion=models.CharField(max_length=300, null=False)
    precio=models.FloatField()
    imagen=models.ImageField(upload_to='foto_prod', blank=True, null=True, default='logo.png')
    clasificacion=models.ForeignKey(Clasificacion, null=True, on_delete=models.SET_NULL)
    codigo=models.OneToOneField(Codigo, blank=True, null=True, on_delete=models.SET_NULL)
    color= models.ManyToManyField(Color)
    slug = models.SlugField(help_text="identifica al producto: ej Prod1 ")
    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse ("/aplicacion1/product", kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={'slug': self.slug})

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} de {self.item.nombre}"

    def get_total_item_price(self):
        return self.quantity * self.item.precio

    def get_final_price(self):
        return self.get_total_item_price()

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    ciudad = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

class Pregunta(models.Model):
    nombre=models.CharField(max_length=50, null=False)
    pregunta=models.CharField(max_length=100, null=False)
    respuesta=models.CharField(max_length=100, null=False)


    def __str__(self):
        return self.pregunta


class Orden(models.Model):
    nombre=models.CharField(max_length=50, null=False)
    descripcion=models.CharField(max_length=100, null=False)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    email=models.EmailField()




