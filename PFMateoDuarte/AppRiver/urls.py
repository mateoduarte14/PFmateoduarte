from django.urls import path
from AppRiver.views import inicio, historia, river_hoy, river_14, socio_formulario, buscar_socio,actividad_formulario,entrada_formulario,entradacopa_formulario, leer_Socios


urlpatterns = [
    path('', inicio,name='Inicio'),
    path('historia/', historia, name= 'Monumental'),
    path('HoyJuegaRiver/', river_hoy, name= 'JuegaRiver'),
    path('Hinchas/',river_14, name= 'Hinchada'),
    path('leersocios',leer_Socios, name = "LeerSocio")
]

forms_api = [
    path('registro-socio', socio_formulario, name= 'SocioFormulario'),
    path('busqueda-socio', buscar_socio, name='SocioBuscar'),
    path('registro-actividad', actividad_formulario, name='ActividadFormulario'),
    path('registro-entrada', entrada_formulario, name='EntradaFormulario'),
    path('registro-entradacopa', entradacopa_formulario, name='EntradaCopaFormulario')
]

urlpatterns += forms_api