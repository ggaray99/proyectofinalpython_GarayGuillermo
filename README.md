### Proyecto Final Python-Coderhouse

#### Consigna

###### Objetivos generales

Desarrollar una WEB Django con patrón MVT subida a Github.
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
La misma dentro cuenta con tres clases:
```
class ActivosAsignados(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
    fecha_de_carga = models.DateField()
    usuario_asignado = models.CharField(max_length=100)
```
Esta primer clase almacenará a quien fue asignado un activo en particular.

```
	class Usuarios(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    puesto = models.CharField(max_length=40)
    sucursal = models.CharField(max_length=40)
```
Aqui cargaremos los usuarios que podran tener asignado un activo.

```
	class TipoActivos(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
```
Y en esta ultima clase guardaremos los activos a asignar luego.

Creamos en views.py las funciones que utilizaremos tanto para poder hacer el POST en una tabla, como asi tambien las funciones para poder hacer la busqueda GET segun un codigo de un activo.

En la pagina de inicio de la WEB nos encontraremos con una barra en la parte superior donde podremos acceder a cada uno de los formularios disponibles, tanto como para cargar datos o para realizar la busqueda.

Espero que la informacion les sea de ayuda!
