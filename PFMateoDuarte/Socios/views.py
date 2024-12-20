from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from Socios.forms import UserRegisterForm, UserEditForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from Socios.models import Avatar

# Create your views here.


def log(request):

      msg_login = ""
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  socio = authenticate(username=usuario, password=contra)

                  if socio is not None:
                        login(request, socio)
                        return render(request,"AppRiver/hijo.html")
                  
            msg_login = "Usuario o Contraseña invalidos"

      form = AuthenticationForm()
      return render(request,"Socios/login.html", {'form':form, "msg_login": msg_login} )


def regist(request):

      msg_register = ""
      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  usuario = form.save()
                  Avatar.objects.create(user=usuario, imagen='avatares/default.png')
                  return render(request,"AppRiver/hijo.html")
            msg_register="Error en los datos ingresados"

      form = UserRegisterForm()     
      return render(request,"Socios/register.html" ,  {"form":form, "msg_register":msg_register})

@login_required
def editar_perfil(request):

      usuario = request.user

      if request.method == 'POST':

            form = UserEditForm(request.POST, request.FILES, instance=usuario)

            if form.is_valid():
                  
                  if form.cleaned_data.get('imagen'):

                        usuario.avatar.imagen = form.cleaned_data.get('imagen')
                        usuario.avatar.save()

                  form.save()

                  return render(request, "AppRiver/hijo.html")
      else:
            form = UserEditForm(instance=request.user)
      
      return render (request, "Socios/editarusuario.html", 
                     {
                           "formulario": form
                     })


class CambiarPassView(LoginRequiredMixin, PasswordChangeView):
      template_name = "Socios/editar_contraseña.html"
      success_url = reverse_lazy('EditarPerfil')
