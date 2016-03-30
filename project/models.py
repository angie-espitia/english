from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Chapter(models.Model):
    name = models.CharField(max_length= 120)


class Topic(models.Model):
    title = models.CharField(max_length = 120)
    page = HTMLField()
    chapter = models.ForeignKey(Chapter)

class Estudiante(models.Model):
    nombre = models.CharField(max_length= 120)
    apellido = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    tel = models.CharField(max_length = 100)
    clave = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 100)
    sexo = models.CharField(max_length = 100)
    fecha_nacimiento = models.CharField(max_length = 100)
    cedula = models.CharField(max_length = 100)
    Foto = models.CharField(max_length = 100)

class Profesor(models.Model):
    nombre = models.CharField(max_length= 120)
    apellido = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    tel = models.CharField(max_length = 100)
    clave = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 100)
    sexo = models.CharField(max_length = 100)
    fecha_nacimiento = models.CharField(max_length = 100)
    cedula = models.CharField(max_length = 100)
    foto = models.CharField(max_length = 100)
    profesion = models.CharField(max_length = 100)
    especialidad = models.CharField(max_length = 100)

class Curso(models.Model):
    nombre = models.CharField(max_length= 120)
    fecha_inicio = models.FloatField()
    fecha_fin = models.FloatField()
    Profesor = models.ForeignKey(Profesor)
    Chapter = models.ManyToManyField(Chapter)
    image = models.ImageField(upload_to = 'uploads/')

class Modulo(models.Model):
    nombre = models.CharField(max_length= 120)
    fecha_inicio = models.FloatField()
    fecha_fin = models.FloatField()
    Curso = models.ForeignKey(Curso)

class Usuario(User):
    class Meta:
        proxy = True

