from django.contrib import admin
from .models import Usuario, Mensaje, Cliente

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Mensaje)
admin.site.register(Cliente)