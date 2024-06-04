from django.urls import path
from AppCoder import views
from .forms import usuariosFormularios
from django.contrib.auth.views import LogoutView, logout_then_login
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('asignarActivos', views.asignarActivos, name="asignarForm"),
    path('usuarios', views.usuario, name="usuarioForm"),
    path('activos', views.asignarTipoActivos, name="tipoactivoForm"),
    path('busqueda', views.buscar_activos, name="buscar_activos"),
    path('buscar/', views.busqueda_activo),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('activos/', views.lista_activos, name='lista_activos'),
    path('activos/<int:pk>/', views.detalle_activo, name='detalle_activo'),
    path('activo/<int:pk>/editar/', views.editar_activo, name='editar_activo'),
    path('activos/<int:pk>/eliminar/', views.eliminar_activo, name='eliminar_activo'),
    path('tipo_activo/', views.lista_tipo_activos, name='lista_tipo_activos'),
    path('tipo_activo/<int:pk>/', views.detalle_tipo_activo, name='detalle_tipo_activo'),
    path('tipo_activo/<int:pk>/', views.eliminar_tipo_activo, name='eliminar_tipo_activo'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),
    path('about', views.about, name="about")
]