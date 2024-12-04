from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "AppRiver/hijo.html")
def hist(request):
    return render(request, "AppRiver/historia.html")
def rivhoy(request):
    return render(request, "AppRiver/hoyjuegariver.html" )
def riv14(request):
    return render(request, "AppRiver/hinchada.html" )