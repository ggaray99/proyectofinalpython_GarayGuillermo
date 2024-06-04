from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class ActivosAsignados(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
    fecha_de_carga = models.DateField()
    usuario_asignado = models.CharField(max_length=100)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    puesto = models.CharField(max_length=40)
    sucursal = models.CharField(max_length=40)


class TipoActivos(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
    fecha_de_carga = models.DateField()

def get_image_filename(instance, filename):
    title =  'titulo'
    slug = slugify(title)
    return "imagenesAvatares/%s-%s" % (slug, filename)  


class Avatar(models.Model):
    #vinvulo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Subcaperta avatares de media :) 
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    

