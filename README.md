# VS - Handmade Shop & More

Este proyecto consiste en el desarrollo de una aplicacion para un negocio independiente, tanto para la presentacion y venta de sus productos.

## Tabla de Contenidos

* [Tecnologias Usadas](#Tecnologias)
* [Instalacion](#Instalacion)
* [Consideraciones](#Consideraciones)
* [Funcionalidad y Visualizacion](#Consideraciones)

<a name="Tecnologias"></a>
## Tecnologias

Este proyecto fue creado usando:
* HTML
* CSS
* Boostrap   (https://getbootstrap.com/)
* JavaScript (https://datatables.net/)
* JQuery    (https://jquery.com/)
* DataTable plugin (https://datatables.net/)
* Python (https://www.python.org/)
* Django (https://www.djangoproject.com/)
* PostgreSQL (https://www.postgresql.org/)
* FancyBox (http://fancybox.net/)
* SweetAlert plugin (https://sweetalert.js.org/)
* FontAwsome (https://fontawesome.com/)
* Cloudinary (https://cloudinary.com/)

<a name="Instalacion"></a>
## Instalacion
Para descargar este proyecto, se debe clonar desde este repositorio remoto a un repositorio local.

$git clone https://github.com/valesc1971/VSHandmadeShop.git

Se debe tambien correr dentro de un entorno virtual de Python (virtualenv) (https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

Las librerías instaladas se encuentran en el archivo requirements.txt

<a name="Consideraciones"></a>
## Consideraciones

Para el desarrollo del código de frontend, se utilizó HTML como herramienta principal. Para el formato, se utilizó CSS y las herramientas JavaScript, JQuery, Boostrap y DataTable, Fancybox las que son llamadas usando CDNs.

Los archivos de HTML se encuentran en una carpeta dentro de la aplicacion (aplicacion1/templates)
 
Se creo una plantilla de html (proyecto/templates/base_layout.html) que contiene el logo de la tienda, la barra de navegacion , el footer y mensajes de alerta, incluyendo tambien los archivos y CDNs para las herramientas de diseño. Esta plantilla se llama dentro de los archivos HTML principales

Los archivos de imagenes, CSS y JS se encuentran dentro de un directorio static (aplicacion1/static)

El desarrollo del codigo de backend se hizo usando la framework django en conjunto con python.

<a name="Funcionalidad y Visualizacion"></a>
## Funcionalidad y Visualizacion

Se puede navegar a través del sitio usando las opciones que entrega la barra de navegación. Estas opciones tienes visibilidad de acuerdo al tipo de usuario que ha ingresado.

En caso ingresado a la aplicacion como visitante sin haber hecho login, se despliegan también opciones reducidas de la barra de navegación, de tal forma que el visitante pueda interactuar, visualizar los productos, enviar mensajes de contacto y registrase como usuario.

Los links incluidos en la barra de navegacion para un usuario que no ha ingresado, son los siguientes:

**•	Inicio:**
![image](https://user-images.githubusercontent.com/99301347/170878320-bb02ca7d-b093-4e30-8338-44c555d60697.png)


**•	Mis trabajos:** presentacion de la tienda y ejemplo de productos
![image](https://user-images.githubusercontent.com/99301347/170878346-ac087829-051d-4336-b314-aa00cd178c49.png)


**•	Productos:**  galeria de productos. Si se hace clic en Ver, se despliega el producto en forma individual aumentado.
![image](https://user-images.githubusercontent.com/99301347/170878373-14f0fa9c-f1ce-408d-9882-cffe78857519.png)

**•	Contacto:** formulario para enviar mensaje. Una vez enviado un mensaje, el usuario recibe un mail de agradecimiento/informativo
![image](https://user-images.githubusercontent.com/99301347/170878409-036613f2-51ae-46fc-a3a0-7f29546ccb08.png)

**•	Menu:** Este menú permite el acceso a registro de visitantes (Inscripcion Club),  Registro de usuarios, Ingresar y Salir

![image](https://user-images.githubusercontent.com/99301347/170877963-34ee3c50-e995-41f3-864f-8f128cb44ce7.png)

En el caso de que el usuario ingrese como usuario activo (cliente), la opcion Productos entrega la opcion de comprar tambien. Si se agrega el producto a la compra, se despliega una pagian donde se presenta el resumen de la compra con la posibilidad de agregar mas producto, cambiar la cantidad del producto, elminar productos y finalizar la compra

![image](https://user-images.githubusercontent.com/99301347/170878631-89ee1db0-4abd-46e3-b67a-ce2cd617a45a.png)
Si se finaliza la compra, se ingresa a una opcion donde se despliega nuevamente el resumen, con la opcion de confirmar la compra. Si se confirma la compra, se recibe una confirmacion por pantalla.

![image](https://user-images.githubusercontent.com/99301347/170878732-cf6d2f77-6776-4c14-8b11-69fcce52cc1d.png)

El cliente puede revisar las ordenes anteriores, en la opcion dentro de Menu "Revisar ordenes anteriores"

![image](https://user-images.githubusercontent.com/99301347/170878868-b9217c03-d4b6-4644-923f-9728ef947948.png)

Si el usuario ingresado se loguea como usaurio staff o superusuario, tiene los mismos permisos. en este caso, a diferencia del usuario -cliente, tiene visibilidad tambien del menu "Admin"

**•	Admin:** Este menú permite el acceso a opciones de usuarios “Staff” o “Superusuarios”. Las opciones que entrega permiten ingresar nuevos productos, ver la lista de productos (editar y elminar productos y descargar lista en archiv excel) , revisar mensajes recibidos de visitantes, y revisar la lista de clientes registrados
 
![image](https://user-images.githubusercontent.com/99301347/170894501-f9a506f8-bae5-4d9f-91b7-e0d6331bbb31.png)

![image](https://user-images.githubusercontent.com/99301347/170894526-2693437a-d478-4d24-8c72-3c99678283cf.png)
 
Para visualizarla, se debe hacer los siguientes cambios en el archivo setting.py
 
 ![image](https://user-images.githubusercontent.com/99301347/169719661-19d5e48f-51d2-4697-81fe-68e7b493821e.png)

 ![image](https://user-images.githubusercontent.com/99301347/169719664-123a21bf-d8e8-4010-bf07-12746ae20b83.png)








