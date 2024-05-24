from django.urls import path
from AppCoder import views
from .forms import usuariosFormularios
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('asignarActivos', views.asignarActivos, name="asignarForm"),
    path('usuarios', views.usuario, name="usuarioForm"),
    path('activos', views.asignarTipoActivos, name="tipoactivoForm"),
    path('busqueda', views.buscar_activos, name="buscar_activos"),
    path('buscar/', views.busqueda_activo),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    path('activos/', views.lista_activos, name='lista_activos'),
    path('activos/<int:pk>/', views.detalle_activo, name='detalle_activo'),
    path('activos/<int:pk>/eliminar/', views.eliminar_activo, name='eliminar_activo'),
    path('editarPerfil/', views.editarPerfil, name='EditarPerfil')
]