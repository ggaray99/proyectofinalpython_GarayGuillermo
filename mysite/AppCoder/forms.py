from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ActivosAsignados, TipoActivos

class usuariosFormularios(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    puesto = forms.CharField(max_length=40)
    sucursal = forms.CharField(max_length=40)

class TipoActivosFormularios(forms.Form):
    codigo = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=255)
    fecha_de_carga = forms.DateField()

class TipoActivosFormularios(forms.ModelForm):
    class Meta:
        model = TipoActivos
        fields = ['codigo', 'descripcion', 'fecha_de_carga']
        widgets = {
            'fecha_de_carga': forms.DateInput(attrs={'type': 'date'})
        }

class ActivosAsignadosFormularios(forms.ModelForm):
    class Meta:
        model = ActivosAsignados
        fields = ['codigo', 'descripcion', 'fecha_de_carga', 'usuario_asignado']
        widgets = {
            'fecha_de_carga': forms.DateInput(attrs={'type': 'date'})
        }

class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    imagen_avatar = forms.ImageField(required=False)

   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    #Acá se definen las opciones que queres modificar del usuario, 
    #Ponemos las básicas
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 


    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class AvatarFormulario(forms.Form):

    #Especificar los campos
    
    imagen = forms.ImageField(required=True)