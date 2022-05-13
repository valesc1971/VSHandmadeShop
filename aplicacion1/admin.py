from django.contrib import admin
from .models import Usuario, Mensaje, Producto, Clasificacion, Codigo, Color, Pregunta

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Mensaje)
admin.site.register(Producto)
admin.site.register(Clasificacion)
admin.site.register(Codigo)
admin.site.register(Color)
admin.site.register(Pregunta)

