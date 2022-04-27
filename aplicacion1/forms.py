from django import forms
from django.db.models import fields
from .models import Mensaje, Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    clave=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields =('rut', 'nombre', 'apellido','edad', 'email', 'clave')

class LoginForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields =('nombre', 'apellido', 'email', 'mensaje')

class LoginExtForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    clave=forms.CharField(widget=forms.PasswordInput)