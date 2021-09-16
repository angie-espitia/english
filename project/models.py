from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone
import datetime

list_sexo = ( ('M', 'Masculino') , ('F', 'Femenino'))
class Estudiante(models.Model):
    id = models.OneToOneField(User, primary_key=True, on_delete=models.DO_NOTHING)
    tel = models.BigIntegerField(null=True)
    direccion = models.CharField(max_length = 100,null=True)
    sexo = models.CharField( max_length=1, choices = list_sexo, null=True)
    fecha_nacimiento = models.DateField (null=True)
    documento = models.BigIntegerField()
    Foto = models.ImageField(upload_to='media',null=True)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = "Estudiantes"

    def __unicode__(self):
        return '%s' % self.documento

class Profesor(models.Model):
    id = models.OneToOneField(User, primary_key=True, on_delete=models.DO_NOTHING)
    cel = models.BigIntegerField()
    fecha_nacimiento = models.DateField()
    cedula = models.BigIntegerField()
    foto = models.ImageField(upload_to='media', null=True, blank=True)
    profesion = models.CharField(max_length = 100)
    especialidad = models.CharField(max_length = 100)

    class Meta:
        verbose_name = 'Profe'
        verbose_name_plural = "Profes"

    def __unicode__(self):
        return '%s' % self.cedula

class Curso(models.Model):
    nombre = models.CharField(max_length= 120)
    Profesor = models.ForeignKey(Profesor, on_delete=models.DO_NOTHING)
    fecha_inicio = models.DateField( blank=True, null=True )
    fecha_fin = models.DateField( blank=True, null=True )

    def __unicode__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length= 120)
    jornada = models.CharField(max_length= 120)
    Curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    def __unicode__(self):
        return self.nombre

class Estado(models.Model):
    descripcion = models.CharField(max_length= 120)

class Actividades(models.Model):
    nombre = models.CharField(max_length= 120)

class Preguntas(models.Model):
    descripcion = models.TextField()
    actividad = models.ForeignKey(Actividades, on_delete=models.DO_NOTHING)
    indice = models.IntegerField( null=True )

class Respuesta(models.Model):
    descripcion = models.TextField()
    pregunta = models.ForeignKey(Preguntas, on_delete=models.DO_NOTHING)
    indice = models.IntegerField( null=True )

class Grupo_Estudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.DO_NOTHING)
    grupo = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    estado = models.ForeignKey(Estado, null=True, on_delete=models.DO_NOTHING)

class Calificacion(models.Model):
    nota = models.FloatField()
    promedio = models.FloatField(null=True)
    detalle = models.CharField(max_length= 200, null=True)
    actividad = models.ForeignKey(Actividades, null=True, on_delete=models.DO_NOTHING)
    grupo_estudiante = models.ForeignKey(Grupo_Estudiante, on_delete=models.DO_NOTHING)

class Log(models.Model):
    usuario = models.IntegerField()
    tipo= models.CharField(max_length=1)
    tiempo= models.DateTimeField(default=datetime.datetime.now)
    accion= models.TextField()
