from django.http import HttpResponse
from django.template import Template, Context
from .models import ActivosAsignados, Usuarios, TipoActivos, Avatar
from django.shortcuts import render, redirect, get_object_or_404
from .forms import usuariosFormularios,ActivosAsignadosFormularios,TipoActivosFormularios, UserRegisterForm,UserEditForm,AvatarFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/index.html')

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
            messages.success(request, 'El registro se ha guardado exitosamente.')
            return render(request, "AppCoder/asignarActivos.html")
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

# Vista para editar un registro
@login_required
def editar_activo(request, pk):
    activo = get_object_or_404(ActivosAsignados, pk=pk)

    if request.method == 'POST':
        form = ActivosAsignadosFormularios(request.POST, instance=activo)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'El registro se ha actualizado exitosamente.')
            return redirect('detalle_activo', pk=activo.pk)
    else:
        form = ActivosAsignadosFormularios(instance=activo)

    return render(request, 'AppCoder/editar.html', {'form': form, 'activo': activo})


# Vista para eliminar un registro
@login_required
def eliminar_activo(request, pk):
    activo = get_object_or_404(ActivosAsignados, pk=pk)
    if request.method == 'POST':
        activo.delete()
        return redirect('lista_activos')
    return render(request, 'AppCoder/eliminar.html', {'activo': activo})

@login_required
def lista_tipo_activos(request):
    tipo_activos = TipoActivos.objects.all()
    return render(request, 'AppCoder/lista_tipo_activos.html', {'tipo_activos': tipo_activos})

@login_required
def detalle_tipo_activo(request, pk):
    tipo_activo = get_object_or_404(TipoActivos, pk=pk)
    return render(request, 'AppCoder/detalle_tipo_activo.html', {'tipo_activo': tipo_activo})

@login_required
def eliminar_tipo_activo(request, pk):
    tipo_activo = get_object_or_404(TipoActivos, pk=pk)
    if request.method == 'POST':
        tipo_activo.delete()
        messages.success(request, 'El tipo de activo ha sido eliminado exitosamente.')
        return redirect('lista_tipo_activos')
    return render(request, 'AppCoder/confirmar_eliminar.html', {'tipo_activo': tipo_activo})

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
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "AppCoder/index.html", {"mensaje": "Usuario Creado :)"})
        else:
            print(form.errors)  # Imprime los errores en la consola
    else:
        form = UserRegisterForm()
    
    return render(request, "AppCoder/registro.html", {"form": form})



def urlImagen():

      return "/media/avatares/logo.png"

def about(request):
    return render(request, 'AppCoder/about.html')