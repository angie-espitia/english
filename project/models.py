from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

list_sexo = ( ('M', 'Masculino') , ('F', 'Femenino'))
class Estudiante(models.Model):
    id = models.OneToOneField(User, primary_key=True, db_column='id')
    tel = models.IntegerField()
    direccion = models.CharField(max_length = 100)
    sexo = models.CharField( max_length=1, choices = list_sexo)
    fecha_nacimiento = models.DateField (db_column= 'Fecha Nacimiento')
    documento = models.IntegerField()
    Foto = models.ImageField(upload_to='/tmp')

    class Meta:
        db_table = 'estudiante'
        managed  = False

class Profesor(models.Model):
    id = models.OneToOneField(User, primary_key=True, db_column='id')
    cel = models.IntegerField()
    fecha_nacimiento = models.DateField(db_column='Fecha Nacimiento')
    cedula = models.IntegerField()
    foto = models.ImageField(upload_to='/tmp')
    profesion = models.CharField(max_length = 100)
    especialidad = models.CharField(max_length = 100)

    class Meta:
        db_table = 'profesores'
        managed  = False

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
    modulo_estudiante = models.IntegerField()

    class Meta:
        db_table = 'calificacion'
        managed = False