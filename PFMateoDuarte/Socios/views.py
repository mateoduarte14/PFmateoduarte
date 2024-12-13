from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from Socios.forms import UserRegisterForm
# Create your views here.


def loguear(request):

      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppRiver/hijo.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"Socios/login.html", {"form": form,"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"Socios/login.html" ,  {"form": form,"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"Socios/login.html", {'form':form} )


def registrar(request):

    if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppRiver/hijo.html" ,  {"mensaje":"Usuario Creado Correctamente"})
    else:
        form = UserRegisterForm()     

    return render(request,"Socios/register.html" ,  {"form":form})