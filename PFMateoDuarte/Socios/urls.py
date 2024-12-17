from django.urls import path
from django.contrib.auth.views import LogoutView
from Socios.views import log, regist
urlpatterns = [
    path('iniciarsesion/', log, name='Login'),
    path('registrar/', regist, name='Registro'),
    path('cerrarsesion/', LogoutView.as_view(template_name='Socios/logout.html'), name='Logout')
]
