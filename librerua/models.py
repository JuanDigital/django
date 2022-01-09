from django.db import models
from datetime import datetime, date 
# Create your models here.
class alumnos(models.Model):
    id=models.AutoField(primary_key=True)
    grado=models.IntegerField(null=True,verbose_name="Grado")
    seccion=models.IntegerField(null=True,verbose_name="Sección")
    nombre=models.CharField(max_length=100,verbose_name="Nombre del Alumno")    
    padre=models.CharField(max_length=100,verbose_name="Nombre del Padre")
    madre=models.CharField(max_length=100,verbose_name="Nombre de la Madre")
    nacimiento=models.PositiveIntegerField(null=True,verbose_name="Año de Nacimiento")
    ingreso=models.PositiveIntegerField(null=True,verbose_name="Año de ingreso")
