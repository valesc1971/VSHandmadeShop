from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut=models.CharField(max_length=15, null=False)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=100, null=False)
    edad=models.IntegerField()
    email=models.EmailField()
    clave=models.CharField(max_length=30)



class Mensaje(models.Model):
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=100, null=False)
    email=models.EmailField()
    mensaje=models.CharField(max_length=500, null=False)
