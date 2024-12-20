from django.shortcuts import render
from AppRiver.models import Socio, Actividad, EntradasTorneoLocal, EntradasCopa
from AppRiver.forms import RegsSocio, BuscaSocio, AnotarActividad, IngresarEntrada, IngresarEntradaCopa
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):
    return render(request, "AppRiver/hijo.html")
@login_required
def historia(request):
    return render(request, "AppRiver/historia.html")

def river_hoy(request):
    return render(request, "AppRiver/hoyjuegariver.html")
@login_required
def river_14(request):
    return render(request, "AppRiver/hinchada.html")
@login_required
def socio_formulario(request):
    if request.method == 'POST':
        form_registrar = RegsSocio(request.POST)

        if form_registrar.is_valid():
            informacion = form_registrar.cleaned_data

            socio = Socio(nombre=informacion['nombre'],apellido=informacion['apellido'],DNI=informacion['DNI'],fecha_nacimiento=informacion['fecha_nacimiento'],categoria_socio=informacion['categoria_socio'],numero_socio=informacion['numero_socio'])
            socio.save()

            return render(request, "AppRiver/hijo.html")
    else:
        form_registrar = RegsSocio()
    
    return render(request, "AppRiver/registrosocio.html", {"form_registrar": form_registrar})
@login_required
def buscar_socio(request):
    if request.method=="POST":
        form_buscar = BuscaSocio(request.POST)

        if form_buscar.is_valid():
            informacion = form_buscar.cleaned_data

            socios = Socio.objects.filter(DNI__icontains=informacion['DNI'])

            return render(request,"AppRiver/muestrasocio.html", {'socios': socios})
    else:
        form_buscar = BuscaSocio()
    return render(request,"AppRiver/dni_buscasocio.html", {"form_buscar":form_buscar})
@login_required
def actividad_formulario(request):
    if request.method == 'POST':
        form_actividad = AnotarActividad(request.POST)

        if form_actividad.is_valid():
            informacion = form_actividad.cleaned_data

            act = Actividad(nombre=informacion['nombre'],cuota=informacion['arancel'])
            act.save()

            return render(request, "AppRiver/hijo.html")
    else:
        form_actividad = AnotarActividad()
    
    return render(request, "AppRiver/registroactividad.html", {"form_actividad": form_actividad})
@login_required
def entrada_formulario(request):
    if request.method == 'POST':
        form_entrada = IngresarEntrada(request.POST)

        if form_entrada.is_valid():
            informacion = form_entrada.cleaned_data

            entrada = EntradasTorneoLocal(sector=informacion['sector'],precio=informacion['precio'])
            entrada.save()

            return render(request, "AppRiver/hijo.html")
    else:
        form_entrada = IngresarEntrada()
    
    return render(request, "AppRiver/registroentrada.html", {"form_entrada": form_entrada})
@login_required
def entradacopa_formulario(request):
    if request.method == 'POST':
        form_entradacopa = IngresarEntradaCopa(request.POST)

        if form_entradacopa.is_valid():
            informacion = form_entradacopa.cleaned_data

            entradacopa = EntradasCopa(sector=informacion['sector'],precio=informacion['precio'])
            entradacopa.save()

            return render(request, "AppRiver/hijo.html")
    else:
        form_entradacopa = IngresarEntrada()
    
    return render(request, "AppRiver/registroentradacopa.html", {"form_entradacopa": form_entradacopa})
@login_required
def leer_socios(request):

      socios = Socio.objects.all()

      contexto = {"socios": socios} 

      return render(request, "AppRiver/leersocio.html",contexto)
@login_required
def eliminar_socio(request, dni_socio):

    socio_borrar = Socio.objects.get(DNI=dni_socio)
    socio_borrar.delete()

    return render(request, "AppRiver/leersocio.html")

class SocioListView(LoginRequiredMixin, ListView):
    model = Socio
    context_object_name = "socios"
    template_name = "AppRiver/socio_lista.html"

class SocioDetailView(LoginRequiredMixin, DetailView):
    model = Socio
    template_name = "AppRiver/socio_detalle.html"

class SocioCreateView(LoginRequiredMixin, CreateView):
    model = Socio
    template_name = "AppRiver/socio_crear.html"
    success_url = reverse_lazy('SocioLista')
    fields = ['nombre', 'apellido', 'DNI', 'fecha_nacimiento', 'categoria_socio', 'numero_socio']

class SocioUpdateView(LoginRequiredMixin, UpdateView):
    model = Socio
    template_name = "AppRiver/socio_modificar.html"
    success_url = reverse_lazy('SocioLista')
    fields = ['nombre', 'apellido', 'DNI', 'fecha_nacimiento', 'categoria_socio', 'numero_socio']

class SocioDeleteView(LoginRequiredMixin, DeleteView):
    model = Socio
    template_name = "AppRiver/socio_eliminar.html"
    success_url = reverse_lazy('SocioLista')

def about(request):
    return render(request, "AppRiver/Aboutme.html")

def lista_urls(request):
    contexto = [
        {'name': 'Historia', 'url': reverse("Monumental")},
        {'name': 'JuegaRiver', 'url': reverse("JuegaRiver")},
        {'name': 'Hinchada', 'url': reverse("Hinchada")},
        {'name': 'About Me', 'url': reverse("About")}
    ]
    return render(request, 'AppRiver/blogs.html', {'contexto':contexto})