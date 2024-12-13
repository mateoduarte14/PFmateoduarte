from django.urls import path
from django.contrib.auth.views import LogoutView
from Socios.views import loguear, registrar
urlpatterns = [
    path('IniciarSesion', loguear, name='Login'),
    path('Registro', registrar, name='Registro'),
    path('CerrarSesion', LogoutView.as_view(template_name='Socios/logout.html'), name='Logout')
]
