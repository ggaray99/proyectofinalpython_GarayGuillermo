### Proyecto Final Python-Coderhouse

#### Consigna

###### Objetivos generales

Desarrollar una WEB Django subida a Github.

###### Video explicativo de la WEB
https://youtu.be/kjlL66YwY1Q

###### Se debe entregar

🕵 Cumplimiento de consigna:
💫 Entrega hecha por GitHub 
💫 Readme con la explicación del proyecto
💫 Video de no más de 10 minutos
🕵 Estructura interna:
💫 una o más aplicaciones creadas
💫 dos modelos con campos de texto, número, fecha
💫 vista de listado de registros de un modelo
💫 vista del detalle de un registro de un modelo
💫 vista para crear un registro de un modelo
💫 vista para eliminar un registro de un modelo
💫 about/ que hable sobre el creador del proyecto
🕵 Lógica de usuarios:
💫 login de usuario
💫 registro de usuario
💫 administrador: puede realizar CRUD sobre los modelos
💫 administrador: subir una imagen de perfil para un usuario
🕵 Flujo del proyecto
💫 Ingresar a la web app desde la ruta base ‘/’ y direccionar a “home”
💫 navegar entre las diferentes URL sin tener que usar la “barra del navegador”

Se realizo el proyecto final en Visual Studio Code, utilizando Python como lenguaje principal y SQLLite como BBDD. También se utilizó DBBrowser para visualizar los datos cargados.

Se tuvieron en cuenta los requisitos de la consigna, creando una WEB Django llamada AppCoder en este caso.

Para poder utilizar la web deberiamos tener instalado la version Python 3.12.3 o superior, ademas de las siguientes librerias

Django==5.0.6
pillow==10.3.0

Una vez tengamos esto instalado podremos poner a correr nuestra web desde VSC o nuestro terminal con el siguiente comando:

python manage.py runserver

En la pagina de inicio de la WEB nos encontraremos con una barra en la parte superior donde podremos acceder a cada uno de los formularios disponibles, tanto como para cargar datos a un formulario, o bien, dentro de una pagina tendremos la posibilidad de listar los registros de un modelo para poder verlo mas en detalle, editarlo o eliminarlo si eso quisieramos. Ademas, contamos con la opcion de iniciar sesion o registrarnos.

Para poder realizar las pruebas podrian utilizar el usuario de prueba que creé en el video explicativo o el usuario admin. Dejo las credenciales aqui abajo para la prueba:

user: usuarioprueba
pass: hola123456

user: admin
pass: admin

Espero que la informacion les sea de ayuda!
