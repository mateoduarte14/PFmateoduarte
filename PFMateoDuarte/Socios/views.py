from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from Socios.forms import UserRegisterForm
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

                  form.save()
                  return render(request,"AppRiver/hijo.html")
            msg_register="Error en los datos ingresados"

      form = UserRegisterForm()     
      return render(request,"Socios/register.html" ,  {"form":form, "msg_register":msg_register})