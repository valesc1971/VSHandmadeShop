from django.urls import path
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
    path('productos_lista/', views.productos_lista, name='productos_lista'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_mensaje/<int:id>/', views.eliminar_mensaje, name='eliminar_mensaje'),
    path('editar_mensaje/<int:id>/', views.editar_mensaje, name='editar_mensaje'),
    path('mensaje_mail/<str:email>/', views.mensaje_mail, name='mensaje_mail'),
    path('ingreso_productos/', views.ingreso_productos, name='ingreso_productos'),
    path('producto_display/', views.producto_display, name='producto_display'),
    path('compra_producto/<int:id>/', views.compra_producto, name='compra_producto'),
    path('order_summary/', views.OrderSummaryView.as_view(), name='order_summary'),
    path('product/<slug>/', views.ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', views.remove_single_item_from_cart, name='remove-single-item-from-cart'),

    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('compra_user/<str:user>', views.compra_user, name='compra_user'),

]






  

