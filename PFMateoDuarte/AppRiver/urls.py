from django.urls import path
from AppRiver.views import inicio, hist, rivhoy, riv14, socio_formulario, buscar_socio,actividad_formulario,entrada_formulario,entradacopa_formulario


urlpatterns = [
    path('', inicio,name='Inicio'),
    path('historia/', hist, name= 'Monumental'),
    path('HoyJuegaRiver/', rivhoy, name= 'JuegaRiver'),
    path('Hinchas/',riv14, name= 'Hinchada')
]

forms_api = [
    path('registro-socio', socio_formulario, name= 'SocioFormulario'),
    path('busqueda-socio', buscar_socio, name='SocioBuscar'),
    path('registro-actividad', actividad_formulario, name='ActividadFormulario'),
    path('registro-entrada', entrada_formulario, name='EntradaFormulario'),
    path('registro-entradacopa', entradacopa_formulario, name='EntradaCopaFormulario')
]

urlpatterns += forms_api