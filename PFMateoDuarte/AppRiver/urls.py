from django.urls import path
from AppRiver.views import inicio, historia, river_hoy, river_14, socio_formulario, buscar_socio,actividad_formulario,entrada_formulario,entradacopa_formulario,SocioListView,SocioCreateView,SocioDeleteView,SocioDetailView,SocioUpdateView,about,lista_urls

urlpatterns = [
    path('', inicio,name='Inicio'),
    path('historia/', historia, name= 'Monumental'),
    path('HoyJuegaRiver/', river_hoy, name= 'JuegaRiver'),
    path('Hinchas/',river_14, name= 'Hinchada'),
    path('About/', about, name='About'),
    path('lista_urls/', lista_urls, name='URLS'),
]

forms_api = [
    path('registro-socio', socio_formulario, name= 'SocioFormulario'),
    path('busqueda-socio', buscar_socio, name='SocioBuscar'),
    path('registro-actividad', actividad_formulario, name='ActividadFormulario'),
    path('registro-entrada', entrada_formulario, name='EntradaFormulario'),
    path('registro-entradacopa', entradacopa_formulario, name='EntradaCopaFormulario')
]

views_class = [
    path('socios/lista', SocioListView.as_view(), name = 'SocioLista' ),
    path('socios/crear', SocioCreateView.as_view(), name = 'SocioCrear' ),
    path('socios/<pk>', SocioDetailView.as_view(), name = 'SocioDetalle' ),
    path('socios/<pk>/modificar', SocioUpdateView.as_view(), name = 'SocioModificar' ),
    path('socios/<pk>/eliminar', SocioDeleteView.as_view(), name = 'SocioEliminar' )
]

urlpatterns += forms_api + views_class