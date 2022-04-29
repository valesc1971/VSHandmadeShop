from django.urls import path, include
from  .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('ejemplo/', views.ejemplo, name='ejemplo'),
    path('formulario_usuario/', views.formulario_usuario, name='formulario_usuario'),
    path('login/', views.login, name='login'),
    path('bienvenido/', views.bienvenido, name='bienvenido'),
    path('salir/', views.salir, name='salir'),
    path('register/', views.register, name='register'),
    path('mostrar_mensaje/', views.mostrar_mensaje, name='mostrar_mensaje'),
    path('login_externo/', views.login_externo, name='login_externo'),
    path('bienvenido_externo/', views.bienvenido_externo, name='bienvenido_externo'),
    path('salir_externo/', views.salir_externo, name='salir_externo'),
    path('registro_cliente/', views.registro_cliente, name='registro_clientes'),
    path('formulario_cliente/', views.formulario_cliente, name='formulario_cliente'),
    path('clientes/', views.clientes, name='clientes'),
    path('salir_cliente/', views.salir_cliente, name='salir_cliente'),




]
