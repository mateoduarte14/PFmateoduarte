from django import forms

class RegsSocio(forms.Form):
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=25)
    DNI = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    categoria_socio = forms.CharField(max_length=30)
    numero_socio = forms.IntegerField()

class BuscaSocio(forms.Form):
    DNI = forms.IntegerField()

class AnotarActividad(forms.Form):
    nombre = forms.CharField(max_length=25)
    arancel = forms.IntegerField()

class IngresarEntrada(forms.Form):
    sector = forms.CharField(max_length=25)
    precio = forms.IntegerField()

class IngresarEntradaCopa(forms.Form):
    sector = forms.CharField(max_length=25)
    precio = forms.IntegerField()