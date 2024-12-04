from django.urls import path
from AppRiver.views import inicio, hist, rivhoy

urlpatterns = [
path('', inicio,name='Inicio'),
path('/historia', hist, name= 'Historia'),
path('/HoyJuegaRiver', rivhoy, name= 'JuegaRiver')
]