from django.db import models

# Create your models here.

class Socio(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    DNI = models.IntegerField()
    fecha_nacimiento = models.DateField()
    categoria_socio = models.CharField(max_length=30)
    numero_socio = models.IntegerField()
    def __str__(self):
        return f'{self.id} | DNI: {self.DNI} | Nombre y Apellido: {self.nombre}{self.apellido} | Categoria: {self.categoria_socio}'

class Actividad(models.Model):
    nombre = models.CharField(max_length=25)
    arancel = models.IntegerField()
    def __str__(self):
        return f'{self.nombre}'

class EntradasTorneoLocal(models.Model):
    sector = models.CharField(max_length=25)
    precio = models.IntegerField()
    def __str__(self):
        return f'Entrada Torneo {self.sector}'
class EntradasCopa(models.Model):
    sector = models.CharField(max_length=25)
    precio = models.IntegerField()
    def __str__(self):
        return f'Entrada Copa {self.sector}'