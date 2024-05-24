from django.http import HttpResponse
from django.template import Template, Context
from .models import ActivosAsignados, Usuarios, TipoActivos, Avatar
from django.shortcuts import render, redirect, get_object_or_404
from .forms import usuariosFormularios,ActivosAsignadosFormularios,TipoActivosFormularios, UserRegisterForm,UserEditForm,AvatarFormulario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

# Create your views here.
def inicio(request):
    miHtml = open("C:/Users/ggaray/Desktop/Pre-Entrega 3/mysite/AppCoder/templates/AppCoder/index.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)


@login_required
def asignarActivos(request):
    if request.method == 'POST':
        asignarForm = ActivosAsignadosFormularios(request.POST)
        print(asignarForm)

        if asignarForm.is_valid():
            informacion = asignarForm.cleaned_data
            activo = ActivosAsignados(
                codigo=informacion['codigo'],
                descripcion=informacion['descripcion'],
                fecha_de_carga=informacion['fecha_de_carga'],
                usuario_asignado=informacion['usuario_asignado']
            )
            activo.save()
            return render(request, "AppCoder/index.html")
    else:
        asignarForm = ActivosAsignadosFormularios()

    return render(request, "AppCoder/asignarActivos.html", {"asignarForm": asignarForm})

# Vista para listar los registros
@login_required
def lista_activos(request):
    activos = ActivosAsignados.objects.all()
    return render(request, 'AppCoder/lista.html', {'activos': activos})

# Vista para el detalle de un registro
@login_required
def detalle_activo(request, pk):
    activo = get_object_or_404(ActivosAsignados, pk=pk)
    return render(request, 'AppCoder/detalle.html', {'activo': activo})

# Vista para eliminar un registro
@login_required
def eliminar_activo(request, pk):
    activo = get_object_or_404(ActivosAsignados, pk=pk)
    if request.method == 'POST':
        activo.delete()
        return redirect('lista_activos')
    return render(request, 'AppCoder/eliminar.html', {'activo': activo})

@login_required
def usuario(request):
    if request.method == 'POST':
        usuarioForm = usuariosFormularios(request.POST)
        print(usuarioForm)

        if usuarioForm.is_valid():
            informacion = usuarioForm.cleaned_data
            usuario = Usuarios(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                puesto=informacion['puesto'],
                sucursal=informacion['sucursal']
            )
            usuario.save()
            return render(request, "AppCoder/index.html")
    else:
        usuarioForm = usuariosFormularios()

    return render(request, "AppCoder/usuarios.html", {"usuarioForm": usuarioForm})


@login_required
def asignarTipoActivos(request):
    if request.method == 'POST':
        tipoactivoForm = TipoActivosFormularios(request.POST)
        print(tipoactivoForm)

        if tipoactivoForm.is_valid():
            informacion = tipoactivoForm.cleaned_data
            tipo = TipoActivos(
                codigo=informacion['codigo'],
                descripcion=informacion['descripcion'],
                fecha_de_carga=informacion['fecha_de_carga']
            )
            tipo.save()
            return render(request, "AppCoder/index.html")
    else:
        tipoactivoForm = TipoActivosFormularios()

    return render(request,  "AppCoder/activos.html", {"tipoactivoForm": tipoactivoForm})

@login_required
def busqueda_activo (request):
    return render(request,"AppCoder/busquedaactivo.html")

@login_required
def buscar_activos(request):
    if request.method == 'GET':
        codigo = request.GET.get('codigo')

        if codigo is not None:
            activos = TipoActivos.objects.filter(codigo__icontains=codigo)
            return render(request, 'AppCoder/busquedaactivo.html', {'activos': activos})
    
    return render(request, 'AppCoder/busquedaactivo.html')

def logout_request(request):
      logout(request)
     
      return redirect("inicio")

def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppCoder/index.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"AppCoder/index.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppCoder/index.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppCoder/login.html", {'form':form} )

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/index.html" ,  {"mensaje":"Usuario Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})

@login_required
def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
            
                  #Datos que se modificarán
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})



@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html

            if miFormulario.is_valid:   #Si pasó la validación de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})


def urlImagen():

      return "/media/avatares/logo.png"