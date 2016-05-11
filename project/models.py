from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

list_sexo = ( ('M', 'Masculino') , ('F', 'Femenino'))
class Estudiante(models.Model):
    id = models.OneToOneField(User, primary_key=True, db_column='id')
    tel = models.IntegerField(max_length = 100)
    direccion = models.CharField(max_length = 100)
    sexo = models.CharField( max_length=1, choices = list_sexo)
    fecha_nacimiento = models.DateField (db_column= 'Fecha Nacimiento')
    documento = models.IntegerField()
    Foto = models.ImageField(upload_to='/tmp')

    class Meta:
        db_table = 'estudiante'
        managed  = False

class Profesor(models.Model):
    nombre = models.CharField(max_length= 120)
    apellido = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    tel = models.CharField(max_length = 100)
    clave = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 100)
    sexo = models.CharField(max_length = 100)
    fecha_nacimiento = models.CharField(max_length = 100) #, db_column= 'Fecha Nacimiento')
    cedula = models.CharField(max_length = 100)
    foto = models.CharField(max_length = 100)
    profesion = models.CharField(max_length = 100)
    especialidad = models.CharField(max_length = 100)

    class Meta:
        db_table = 'profesores'
        managed  = False
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'


    def __unicode__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length= 120)
    fecha_inicio = models.FloatField()#db_column= 'Fecha_inicio')
    fecha_fin = models.FloatField()#db_column= 'Fecha_fin')
    Profesor = models.ForeignKey(Profesor, db_column='profesores_id')
    #image = models.ImageField(upload_to = 'uploads/')

    class Meta:
        db_table = 'curso'
        managed  = False

    def __unicode__(self):
        return self.nombre

class Modulo(models.Model):
    nombre = models.CharField(max_length= 120)
    fecha = models.FloatField()
    Curso = models.ForeignKey(Curso) #, db_column='curso_id')

    class Meta:
        db_table = 'modulo'
        managed  = False

class Estado(models.Model):
    descripcion = models.CharField(max_length= 120)

    class Meta:
        db_table = 'estado'
        managed  = False

class Calificacion(models.Model):
    Estudiante = models.ForeignKey(Estudiante, db_column='estudiante_id')
    nota = models.FloatField()
    modulo_estudiante = models.ForeignKey(Modulo ,db_column='modulo_id')

    class Meta:
        db_table = 'project_calificacion'
        managed = False