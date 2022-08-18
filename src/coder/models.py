from distutils.command import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}, {self.entregado}"


class Avatar(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null=True, blank=True)
    