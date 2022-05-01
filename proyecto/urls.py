"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from aplicacion1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplicacion1.urls')),
<<<<<<< HEAD
=======
    #path('login/', LoginView.as_view(template_name='aplicacion1/login.html'), name='login'),
    #path('logout/', LogoutView.as_view(template_name='aplicacion1/logout.html'), name='logout'),
    #path('login_cliente/', views.login_cliente, name='login_cliente'),
>>>>>>> 41a720e110324483b7bfcea52a0d3f4c92f7c074
]

handler404 = "aplicacion1.views.page_not_found_view"