from django import forms
from django.db.models import fields

from aplicacion1.validators import validarRut, check_pass_size
from .models import Mensaje, Orden, Usuario, Producto, Orden
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UsuarioForm(forms.ModelForm):
    receive_newsletter = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    rut=forms.CharField(validators=[validarRut])
    class Meta:
        model = Usuario
        fields =( 'nombre', 'apellido','edad', 'email')

               

class LoginForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields =('id','nombre', 'apellido', 'email', 'mensaje') 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields =('nombre', 'descripcion', 'precio', 'clasificacion', 'codigo', 'color', 'imagen') 

class EmailForm(forms.Form):
    email=forms.EmailField()

class OrdenForm(forms.ModelForm):
   
    class Meta:
        model = Orden
        fields =('nombre', 'descripcion', 'precio', 'cantidad', 'email')





