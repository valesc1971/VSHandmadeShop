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
* DataTable plugin (https://datatables.net/)
* Python (https://www.python.org/)
* Django (https://www.djangoproject.com/)
* PostgreSQL (https://www.postgresql.org/)
* FancyBox (http://fancybox.net/)
* SweetAlert plugin (https://sweetalert.js.org/)

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

- inicio, Mis trabajosy productos: presentacion de la tienda y productos
- contacto: formulario para enviar mensaje 
- revisar mensaje: lista todos los mensajes enviados
- Registro_Clientes: formulario para registro de clientes (no para ingresar con usuario) y poder recibir informacion de la tienda
- lista datos de clientes:  lista de clientes y sus datos
- Registro Usuarios: registro de nuevo usuario
- Ingresar: ingreso a la pagina
- Salir: salida de usuario

El desarrollo del codigo de backend se hizo usando la framework django en conjunto con python.

Existe un superusuario creado y se agrego la opcion de registro de nuevos usuarios a traves del sitio con la opcion "Registro Usuarios" en la barra de navegacion.

El sitio tambien permite el ingreso de usuarios ya registrados a traves de la opcion "Ingresar". Una avez que el usuario ingresa, se despliega un mensaje de bienvenida personalizado, y el nombre aparece en la esquina superiror derecha con el tipo de usuario registrado.

La opcion "Salir" permite al usuario desconectarse.


Se crearon tambien 2 modelos (Usuarios y Mensajes) las que almacenas datos de usuarios y mensajes enviados. Estas clases se pueden tambien accesar desde la barra de navegacion en la opcion "Ingresar Datos Usuario" y "Contacto". Estos ingresos se pueden visualizar desde el sitio en "Lista Datos Usuarios" y en "Revisar Mensajes".Se creo ademas un tercer modelo (Productos) para listar los productos y su precio.

![image](https://user-images.githubusercontent.com/99301347/167272247-5d273e20-66a7-4f8c-8d7c-41e721970ecf.png)

La tabla/modelo usuarios permite registrar clientes  solo con sus datos y se pueden ver en su totalidad desde la opcion "Lista Datos clientes" habiendo ingresado como superusuario o staff

![image](https://user-images.githubusercontent.com/99301347/167272297-810df10e-88c3-4221-b556-05b48c8e9640.png)

Se realizo la migracion de las tablas desde SQLite a PostgreSQL.

El sitio presenta tambien 3 restricciones: Las opciones "Revisar Mensajes", "Ingresar Datos Usuarios" y "Lista Datos Usuarios" tiene restricciones de acceso, por lo que el usuario debe havbe ingresado antes de poder revisar estas opciones. Las restricciones se hicieron usando el decorador @login_required
![image](https://user-images.githubusercontent.com/99301347/165001674-0dd6aba9-3803-42a3-b02e-8bec3f47352b.png)

Las opciones en la barra de navegacion se depliegan dependiendo del tipo de usuario que ingresa. 

![image](https://user-images.githubusercontent.com/99301347/167272001-ac4081c5-421d-4634-98c7-b50d7ac57030.png)
![image](https://user-images.githubusercontent.com/99301347/167272012-8578e7e6-ab4c-4b0f-baca-fc3830eda9ec.png)
![image](https://user-images.githubusercontent.com/99301347/167272023-a318d0f4-7271-46e7-96f1-a86734d666c0.png)

si el usuario no ha ingresado, se despliegan las siguientes opciones
![image](https://user-images.githubusercontent.com/99301347/167272039-c5f56132-69f9-4390-bd95-dc6298db4c60.png)

Los mensajes enviados a traves de la pagina contacto, se pueden editar, borrar y visualizar en forma filtrada por el email que se quiere. si se esta ingresado como superusuario/staff, estos se pueden modificar desde el link "revisar mensajes"

![image](https://user-images.githubusercontent.com/99301347/167272141-0ba24bad-865c-4c72-adfe-01b0cc2d5d86.png)

Si el usuario ha ingresado como usuario activo (cliente), solamente puede visualizar, editar o eliminar los mensajes que estan bajo su email. De esta forma, puede entrar a la opcion "contacto" y desde ahi revisar sus mensajes

![image](https://user-images.githubusercontent.com/99301347/167272192-813ce20c-67e0-4c3f-b133-f7f86f2f5d02.png)
![image](https://user-images.githubusercontent.com/99301347/167272204-e318bc46-d6c0-405d-8f37-03b5501ea8eb.png)

Para realizar el ejercicio de relaciones entre modelos, se uso el modelo anterior "Producto" y se creo un formulario para el ingreso de nuevos productos

![image](https://user-images.githubusercontent.com/99301347/168374442-c20ba438-5d69-476d-9e1f-abc65c107d1c.png)
De estaa forma, se crearon los modelos Clasificacion, Codigo, Color con los siguientes tipos de relaciones con el model Producto


Clasificacion: uno a muchos
Codigo: uno a uno
Color: muchos a muchos

![image](https://user-images.githubusercontent.com/99301347/168374470-7db60eb4-c896-4065-8604-b3985efcbff0.png)

De esta forma, cuando se ingresa un nuevo producto a traves del formulario 8o admin), se puede elegir de distintas clasificaciones 8pero solo 1 clasificacion para el producto), se pued tomar solo 1 codigo (1 codigo para cada producto sin repetirse) y se pueden elegir mas de 1 color para 1 solo producto. La lista de los productos se puede visualizar en la tabla Productos que se puede accesar desde la barra de navegacion

![image](https://user-images.githubusercontent.com/99301347/168375038-ad4cd24c-ec6b-440a-9f09-cfa2c19d39f7.png)

Para realizar el ejercicio de migraciones (revertir y restaurar) se creo un nuevo modelo "Pregunta"

Se implemento la personalizacion de la pagina de error 404, sin embargo no es posible activarla considerando que su implementacion significa llevar un ambiente de produccion donde los archivos estaticos no son reconocidos, por lo que los archivs de estilo e imagenes se desactivan. 

Para visualizarla , se debe hacer los siguientes cambios en el archivo setting.py

![image](https://user-images.githubusercontent.com/99301347/165001933-c798ab09-278a-4643-85cb-915ce48acefc.png)

![image](https://user-images.githubusercontent.com/99301347/165001916-d75238cd-4bba-4933-aa28-9a56a64d0b7a.png)


<a name="Visualizacion"></a>
## Visualizacion del sitio web

![image](https://user-images.githubusercontent.com/99301347/167272422-5737057c-9fa6-4915-a5ac-8233396d8245.png)

![image](https://user-images.githubusercontent.com/99301347/167272436-f4306a4d-58b8-44ab-975e-05d1b0debb44.png)
![image](https://user-images.githubusercontent.com/99301347/167272444-ae9dc113-b0b1-470f-843c-049bcca455dd.png)
![image](https://user-images.githubusercontent.com/99301347/167272451-f3009b0b-b79e-4415-bac1-e40805ce6213.png)

![image](https://user-images.githubusercontent.com/99301347/167272464-d130f4e1-c18e-4d8b-bb8a-ef64d048d5a6.png)
![image](https://user-images.githubusercontent.com/99301347/167272468-92ef594e-03b5-46c9-a53c-8f6b8aa7d591.png)
![image](https://user-images.githubusercontent.com/99301347/167272472-3a60f615-7f8b-4f3a-85b2-c68844fb5388.png)
![image](https://user-images.githubusercontent.com/99301347/167272477-00c37e4a-9a8e-4deb-8f02-02c02eb42bbf.png)
![image](https://user-images.githubusercontent.com/99301347/167272486-eb06dcc3-3edb-4011-a03a-5d7f53da7919.png)











