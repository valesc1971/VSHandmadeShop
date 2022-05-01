# Proyecto Individual - VS - Handmade Shop & More

Este proyecto consiste en el desarrollo de un sitio web para un negocio independiente

El objetivo de este sitio es presentar a la empresa y sus productos / servicios, que permita la interaccion con clientes (compras y mensajes / comentario) y la administracion de este (datos usuarios)

En el futuro, se espera implementar un sistema de compras, restricciones de acceso para usuarios (clientes / administradores) y la diferenciacion de sitios de compra y de administracion.

## Tabla de Contenidos

* [Tecnologias Usadas](#Tecnologias)
* [Instalacion](#Instalacion)
* [Consideraciones](#Consideraciones)
* [Visualizacion del sitio web](#Visualizacion)

<a name="Tecnologias"></a>
## Tecnologias

Este proyecto fue creado usando:
* HTML
* CSS
* Boostrap   (https://getbootstrap.com/)
* JavaScript (https://datatables.net/)
* JQuery    (https://jquery.com/)
* DataTable plugin
* Python (https://www.python.org/)
* Django (https://www.djangoproject.com/)

<a name="Instalacion"></a>
## Instalacion
Para descargar este proyecto, se debe clonar desde este repositorio remoto a un repositorio local.

$git clone https://github.com/valesc1971/ProyectoIndividual_Ejercicio5.git

Se debe tambien correr dentro de un entorno virtual de Python (virtualenv) (https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)


<a name="Consideraciones"></a>
## Consideraciones

Para el desarrollo del codigo de frontend, se utilizo HTML como herramienta principal, utilizando tambien CSS para el formato y las herramientas JavaScript, JQuery, Boostrap y DataTable, las que son llamadas usando CDN.

Los archivos de HTML se encuentran en una carpeta dentro de la aplicacion (aplicacion1/templates)

![image](https://user-images.githubusercontent.com/99301347/165000522-6ab8054f-f504-4c06-8931-83a8b3b931b4.png)

Se creo una plantilla de html (proyecto/templates/base_layout.html) que contiene el logo de la tienda, la barra de navegacion y el footer de tal forma de usar el principio de diseño DRY, usando el concepto de block content para llamar el template dentro de los archivos HTML principales. Este template tambien los archivos y CDNs para las herramientas de diseno. 

![image](https://user-images.githubusercontent.com/99301347/165000570-cf061c88-3a04-428f-9285-cdbb4b317690.png)
![image](https://user-images.githubusercontent.com/99301347/165001200-e6fb0145-739f-4262-9285-5bdb41faa3a2.png)
![image](https://user-images.githubusercontent.com/99301347/165001210-c621bc8c-707f-45e5-adb1-0359df5c4e5a.png)



Los archivos de imagenes, CSS y JS se encuentran dentro de un directorio static (aplicacion1/static)

![image](https://user-images.githubusercontent.com/99301347/165000835-65e94099-229a-4122-906b-a3f485a1e869.png)

Se puede navegar a traves del sitio usando las opciones que entrega la barra de navegacion

- inicio y productos: presentacion de la tienda y productos
- contacto: formulario para enviar mensaje 
- revisar mensaje: lista todos los mensajes enviados
- ingresar datos usuarios: formulario para ingresar datos del usuario
- lista datos de usuario:  lista de usuarios y sus datos
- Registrarse: registro de nuevo usuario
- Ingresar: ingreso a la pagina
- Salir: salida de usuario


El desarrollo del codigo de backend se hizo usando la framework django en conjunto con python.

Existe un superusuario creado y se agrego la opcion de registro de nuevos usuarios a traves del sitio con la opcion "Registrarse" en la barra de navegacion.

El sitio tambien permite el ingreso de usuarios ya registrados aa traves de la opcion "Ingresar". Una avez que el usuario ingresa, se despliega un mensaje de bienvenida personalizado, y el nombre aparece en la esquina superiror derecha con el tipo de usuario registrado.

La opcion "Salir" permite al usuario desconectarse.

Se crearon tambien 2 modelos (Usuarios y Mensajes) las que almacenas datos de usuarios y mensajes enviados. Estas clase se pueden tambien accesarse desde la barra de navegacion en la opcion "Ingresar Datos Usuario" y "Contacto". Estos ingresos se pueden visualizar desde el sitio en "Lista Datos Usuarios" y en "Revisar Mensajes"

El sitio presenta tambien 3 restricciones: Las opciones "Revisar Mensajes", "Ingresar Datos Usuarios" y "Lista Datos Usuarios" tiene restricciones de acceso, por lo que el usuario debe havbe ingresado antes de poder revisar estas opciones. Las restricciones se hicieron usando el decorador @login_required

![image](https://user-images.githubusercontent.com/99301347/165001674-0dd6aba9-3803-42a3-b02e-8bec3f47352b.png)

Se implemento la personalizacion de la pagina de error 404, sin embargo no es posible activarla considerando que su implementacion significa llevar un ambiente de produccion donde los archivos estaticos no son reconocidos, por lo que los archivs de estilo e imagenes se desactivan. 

Para visualizarla , se debe hacer los siguientes cambios en el archivo setting.py

![image](https://user-images.githubusercontent.com/99301347/165001933-c798ab09-278a-4643-85cb-915ce48acefc.png)

![image](https://user-images.githubusercontent.com/99301347/165001916-d75238cd-4bba-4933-aa28-9a56a64d0b7a.png)


<a name="Visualizacion"></a>
## Visualizacion del sitio web
![image](https://user-images.githubusercontent.com/99301347/165000180-bbbe6f55-f3a2-4e01-9eee-b6c50368d2d9.png)
![image](https://user-images.githubusercontent.com/99301347/165000228-a2d3820c-69e4-419c-82a9-418d65a6d6d1.png)
![image](https://user-images.githubusercontent.com/99301347/165000236-cc322c14-04d9-40cc-9d94-8115223f627a.png)
![image](https://user-images.githubusercontent.com/99301347/165000295-555da441-df8f-48f3-a05f-fb8c051b58eb.png)
![image](https://user-images.githubusercontent.com/99301347/165000299-54e89761-8724-418f-b1d1-abf5328af826.png)
![image](https://user-images.githubusercontent.com/99301347/165000307-02276d4d-c45c-4600-9ce6-8b94bba606eb.png)
![image](https://user-images.githubusercontent.com/99301347/165000318-025028dd-8ab3-471a-b8dd-7eaa67036b57.png)









