from django.contrib.auth.models import AbstractUser
from django.db import models

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
    precio=models.IntegerField()
    clasificacion=models.ForeignKey(Clasificacion, null=True, on_delete=models.SET_NULL)
    codigo=models.OneToOneField(Codigo, blank=True, null=True, on_delete=models.SET_NULL)
    color= models.ManyToManyField(Color)
    
    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    nombre=models.CharField(max_length=50, null=False)
    pregunta=models.CharField(max_length=100, null=False)
    respuesta=models.CharField(max_length=100, null=False)


    def __str__(self):
        return self.pregunta