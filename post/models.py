from django.db import models
from datetime import date
##from .models import Empleado

# Create your models here.

# clase 

class Empleado(models.Model):
  nombre = models.CharField(max_length=100)
  apellido = models.CharField(max_length=100)
  cargo =  models.CharField(max_length=200)
  funcion =  models.TextField(max_length=200)
  rol= models.TextField(max_length=200)
  fecha_contrato  =  models.DateField(default=date.today)
 ## autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo User de Django
 
class Empresa (models.Model):
  nit= models,models.IntegerField(max_length=8)
  nombre_emp=models.CharField(max_length=100)
  direccion=models.CharField(max_length=100)
  empleado = models.OneToOneField(Empleado, on_delete= models.CASCADE, primary_key = True, null= False)
  
  