from django.urls import path
from AppRiver.views import inicio, hist, rivhoy, riv14

urlpatterns = [
path('', inicio,name='Inicio'),
path('historia', hist, name= 'Monumental'),
path('HoyJuegaRiver', rivhoy, name= 'JuegaRiver'),
path('Hinchas',riv14, name= 'Hinchada')
]