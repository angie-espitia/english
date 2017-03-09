# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import auth
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from .validator import FormRegistroValidator, FormLoginValidator
from english.settings import STATIC_ROLS, EMAIL_HOST_USER, STATICFILES_DIRS
from .models import Estudiante, Profesor, Preguntas, Respuesta, Curso, Grupo, Grupo_Estudiante, Log, Calificacion, Actividades
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from .forms import GrupoForm, CursoForm, CalificacionForm
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DeleteView, CreateView
import json

def index(request):
    return render_to_response('index.html')

def curso(request):
    return render_to_response('../templates/curso.html')

def contacto(request):
    return render_to_response('../templates/contacto.html')

def contacto_f(request):
    return render_to_response('../templates/contacto-f')

# Función login de acceso
def login_estudiante(request):

    if request.method == 'POST':

        validators = FormLoginValidator(request.POST)

        if validators.is_valid():

            auth.login(request, validators.acceso)  # Crear una sesion
            log(request, "INICIO_SESION")
            return HttpResponseRedirect('/inicio-estudiante')

        else:
            return render_to_response('../templates/login-estudiante.html', {'error': validators.getMessage()} , context_instance = RequestContext(request))

    return render_to_response('../templates/login-estudiante.html', context_instance=RequestContext(request))

def login_profesor(request):

    if request.method == 'POST':
        validator = FormLoginValidator(request.POST)

        if validator.is_valid():

            usuario = request.POST['usuario']
            clave = request.POST['clave']
            auth.login(request, validator.acceso)  # Crear una sesion
            return HttpResponseRedirect('/home')
        else:
            return render_to_response('../templates/login-profe.html', {'error': validator.getMessage()} , context_instance = RequestContext(request))

    return render_to_response('../templates/login-profe.html', context_instance=RequestContext(request))

def restringir_estudiante(User):
     if User.groups.filter(id = STATIC_ROLS['Estudiantes']).exists():
         return False
     elif User.groups.filter(id=STATIC_ROLS['Profesores']).exists():
         return True
     else:
        return True

def restringir_profe_inicioest(User):
     if User.groups.filter(id = STATIC_ROLS['Estudiantes']).exists():
         return True
     elif User.groups.filter(id=STATIC_ROLS['Profesores']).exists():
         return False
     else:
        return True

@login_required(login_url="/login-estudiante")
def logout(request):
    log(request, "CERRO_SESION")
    auth.logout(request)
    return redirect('index')

@login_required(login_url="/login-estudiante")
@user_passes_test(restringir_profe_inicioest, login_url='/login-profesor')
def inicio_estudiante(request):
    usuario = Estudiante.objects.get(id=request.user.id)
    log(request, "INICIO_ESTUDIANTE")
    return render(request, 'paginaEstudiante/inicio-estudiante.html', { 'usuario': usuario })

@login_required(login_url="/login-estudiante")
def perfil_estudiante(request):
    usuario = Estudiante.objects.get(id=request.user.id)
    log(request, "PERFIL_ESTUDIANTE")
    return render(request, 'paginaEstudiante/perfil-estudiante.html', { 'usuario': usuario })

@login_required(login_url="/login-estudiante")
def modificar_perfil_est(request):
    error = False
    if request.method == 'POST':
        usu = User.objects.get( id = request.user.id )
        usu.email = request.POST['email']
        usu.save()

        miusuario = Estudiante()
        miusuario.id = usu
        miusuario.documento = request.POST.get('documento')
        miusuario.tel = request.POST.get('tel')
        miusuario.direccion = request.POST.get('direccion')
        miusuario.fecha_nacimiento = request.POST.get('nacimiento')
        miusuario.save()

        log(request, "PERFIL_EDITADO")

        if request.user.groups.filter(id=STATIC_ROLS['Estudiantes']).exists():
            usuario_int = Estudiante.objects.get(id__id=request.user.id)
        else:
            usuario_int = None

    log(request, "PAGINA_PERFIL")
    return render(request, 'paginaEstudiante/perfil-estudiante.html',{ "usuario":  miusuario } )

@login_required(login_url="/login-estudiante")
def modificar_contra_estudiante(request):
    error = False
    usu1 = None
    if request.method == 'POST':
        usu1 = User.objects.get(id=request.user.id)
        usu1.password = make_password(request.POST['password1'])
        usu1.save()
        log(request, "CONTRASEÑA_MODIFICADA")
    return render(request, 'paginaEstudiante/perfil-estudiante.html', { 'usuario': usu1 } )

@login_required(login_url="/login-estudiante")
def multimedia(request):
    log(request, "MULTIMEDIA")
    return render(request, 'contenidos/multimedia.html')

# <---------------------------------- modulo 1 -----------------------------------------------------
@login_required(login_url="/login-estudiante")
def modulo1(request):
    log(request, "CONTENIDO_MODULO1")
    return render(request, 'contenidos/unidad1/modulo1.html')

@login_required(login_url="/login-estudiante")
def modulo1_unidad1(request):
    log(request, "CONTENIDO_MODULO1_UNIDAD1")
    return render(request, 'contenidos/unidad1/modulo1-unidad1.html')

@login_required(login_url="/login-estudiante")
def modulo1_unidad2(request):
    log(request, "CONTENIDO_MODULO1_UNIDAD2")
    return render(request, 'contenidos/unidad1/modulo1-unidad2.html')

@login_required(login_url="/login-estudiante")
def modulo1_unidad3(request):
    log(request, "CONTENIDO_MODULO1_UNIDAD3")
    return render(request, 'contenidos/unidad1/modulo1-unidad3.html')

@login_required(login_url="/login-estudiante")
def unidad1_tm1(request):
    log(request, "CONTENIDO_MODULO1_LESSON1_TEMA1")
    return render(request, 'contenidos/unidad1/modulo1-unidad1 -tm1.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson1_tm2(request):
    log(request, "CONTENIDO_MODULO1_LESSON1_TEMA2")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson1-tm2.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson1_tm3(request):
    log(request, "CONTENIDO_MODULO1_LESSON1_TEMA3")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson1-tm3.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson1_tm4(request):
    log(request, "CONTENIDO_MODULO1_LESSON1_TEMA4")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson1-tm4.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson2_tm1(request):
    log(request, "CONTENIDO_MODULO1_LESSON2_TEMA1")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson2-tm1.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson2_tm2(request):
    estudiante = User.objects.get(id=request.user.id)
    preguntas = Preguntas.objects.filter(actividad_id=1)
    respuesta = Respuesta.objects.filter(pregunta__in = preguntas)
    log(request, "CONTENIDO_MODULO1_LESSON2_TEMA2")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson2-tm2.html', { 'respuesta':respuesta } )

@login_required(login_url="/login-estudiante")
def unidad1_lesson2_tm3(request):
    log(request, "CONTENIDO_MODULO1_LESSON2_TEMA3")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson2-tm3.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson2_tm4(request):
    log(request, "CONTENIDO_MODULO1_LESSON2_TEMA4")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson2-tm4.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson3_tm1(request):
    log(request, "CONTENIDO_MODULO1_LESSON3_TEMA1")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson3-tm1.html' ) 

@login_required(login_url="/login-estudiante")
def unidad1_lesson3_tm2(request):
    estudiante = User.objects.get(id=request.user.id)
    preguntas = Preguntas.objects.filter(actividad_id=2)
    preguntas2 = Preguntas.objects.filter(actividad_id=3)
    preguntas3 = Preguntas.objects.filter(actividad_id=4)
    respuesta = Respuesta.objects.filter(pregunta__in = preguntas)
    respuesta2 = Respuesta.objects.filter(pregunta__in = preguntas2)
    respuesta3 = Respuesta.objects.filter(pregunta__in = preguntas3)
    log(request, "CONTENIDO_MODULO1_LESSON3_TEMA2")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson3-tm2.html', { 'respuesta':respuesta, 'respuesta2':respuesta2, 'respuesta3':respuesta3, 'estudiante':estudiante }) 

@login_required(login_url="/login-estudiante")
def unidad1_lesson3_tm3(request):
    log(request, "CONTENIDO_MODULO1_LESSON3_TEMA3")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson3-tm3.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson3_tm4(request):
    log(request, "CONTENIDO_MODULO1_LESSON3_TEMA4")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson3-tm4.html')  

@login_required(login_url="/login-estudiante")
def unidad1_lesson4_tm1(request):
    log(request, "CONTENIDO_MODULO1_LESSON4_TEMA1")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson4-tm1.html')  

@login_required(login_url="/login-estudiante")
def unidad1_lesson4_tm2(request):    
    estudiante = User.objects.get(id=request.user.id)
    preguntas = Preguntas.objects.filter(actividad_id=11)
    respuesta = Respuesta.objects.filter(pregunta__in = preguntas)
    log(request, "CONTENIDO_MODULO1_LESSON4_TEMA2")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson4-tm2.html',{ 'respuesta':respuesta })  

@login_required(login_url="/login-estudiante")
def unidad1_lesson4_tm3(request):
    log(request, "CONTENIDO_MODULO1_LESSON4_TEMA3")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson4-tm3.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson4_tm4(request):
    log(request, "CONTENIDO_MODULO1_LESSON4_TEMA4")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson4-tm4.html')   

@login_required(login_url="/login-estudiante")
def unidad1_lesson5_tm1(request):
    estudiante = User.objects.get(id=request.user.id)
    preguntas = Preguntas.objects.filter(actividad_id=5)
    respuesta = Respuesta.objects.filter(pregunta__in = preguntas)
    log(request, "CONTENIDO_MODULO1_LESSON5_TEMA1")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson5-tm1.html', { 'respuesta':respuesta } )    

@login_required(login_url="/login-estudiante")
def unidad1_lesson5_tm2(request):
    estudiante = User.objects.get(id=request.user.id)
    preguntas = Preguntas.objects.filter(actividad_id=6)
    preguntas2 = Preguntas.objects.filter(actividad_id=7)
    respuesta = Respuesta.objects.filter(pregunta__in = preguntas)
    respuesta2 = Respuesta.objects.filter(pregunta__in = preguntas2)
    log(request, "CONTENIDO_MODULO1_LESSON5_TEMA2")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson5-tm2.html', { 'respuesta':respuesta, 'respuesta2':respuesta2 })    

@login_required(login_url="/login-estudiante")
def unidad1_lesson5_tm3(request):
    log(request, "CONTENIDO_MODULO1_LESSON5_TEMA3")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson5-tm3.html')   

@login_required(login_url="/login-estudiante")
def unidad1_lesson5_tm4(request):
    log(request, "CONTENIDO_MODULO1_LESSON5_TEMA4")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson5-tm4.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson6_tm1(request):    
    estudiante = User.objects.get(id=request.user.id)
    preguntas = Preguntas.objects.filter(actividad_id=8)
    respuesta = Respuesta.objects.filter(pregunta__in = preguntas)
    log(request, "CONTENIDO_MODULO1_LESSON6_TEMA1")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson6-tm1.html', { 'respuesta':respuesta }) 

@login_required(login_url="/login-estudiante")
def unidad1_lesson6_tm2(request):    
    estudiante = User.objects.get(id=request.user.id)
    preguntas = Preguntas.objects.filter(actividad_id=9)
    preguntas2 = Preguntas.objects.filter(actividad_id=10)
    respuesta = Respuesta.objects.filter(pregunta__in = preguntas)
    respuesta2 = Respuesta.objects.filter(pregunta__in = preguntas2)
    log(request, "CONTENIDO_MODULO1_LESSON6_TEMA2")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson6-tm2.html', { 'respuesta':respuesta, 'respuesta2':respuesta2, 'preguntas':preguntas  }) 

@login_required(login_url="/login-estudiante")
def unidad1_lesson6_tm3(request):
    log(request, "CONTENIDO_MODULO1_LESSON6_TEMA3")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson6-tm3.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson6_tm4(request):
    log(request, "CONTENIDO_MODULO1_LESSON6_TEMA4")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson6-tm4.html')  

@login_required(login_url="/login-estudiante")
def unidad1_lesson7_tm1(request):
    log(request, "CONTENIDO_MODULO1_LESSON7_TEMA1")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson7-tm1.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson7_tm2(request):
    log(request, "CONTENIDO_MODULO1_LESSON7_TEMA2")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson7-tm2.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson7_tm3(request):
    log(request, "CONTENIDO_MODULO1_LESSON7_TEMA3")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson7-tm3.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson7_tm4(request):
    log(request, "CONTENIDO_MODULO1_LESSON7_TEMA4")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson7-tm4.html')  

@login_required(login_url="/login-estudiante")
def unidad1_lesson8_tm1(request):
    log(request, "CONTENIDO_MODULO1_LESSON8_TEMA1")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson8-tm1.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson8_tm2(request):
    log(request, "CONTENIDO_MODULO1_LESSON8_TEMA2")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson8-tm2.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson8_tm3(request):
    log(request, "CONTENIDO_MODULO1_LESSON8_TEMA3")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson8-tm3.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson8_tm4(request):
    log(request, "CONTENIDO_MODULO1_LESSON8_TEMA4")
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson8-tm4.html')                  

# <---------------------------- modulo 2 ------------------------------------------
@login_required(login_url="/login-estudiante")
def modulo2(request):
    log(request, "CONTENIDO_MODULO2")
    return render(request, 'contenidos/unidad2/modulo2.html')

@login_required(login_url="/login-estudiante")
def modulo2_unidad1(request):
    log(request, "CONTENIDO_MODULO2_UNIDAD1")
    return render(request, 'contenidos/unidad2/modulo2-unidad1.html')

@login_required(login_url="/login-estudiante")
def modulo2_unidad2(request):
    log(request, "CONTENIDO_MODULO2_UNIDAD2")
    return render(request, 'contenidos/unidad2/modulo2-unidad2.html')

@login_required(login_url="/login-estudiante")
def modulo2_unidad3(request):
    log(request, "CONTENIDO_MODULO2_UNIDAD3")
    return render(request, 'contenidos/unidad2/modulo2-unidad3.html')

@login_required(login_url="/login-estudiante")
def modulo2_unidad1_lesson1_tm1(request):
    log(request, "CONTENIDO_MODULO2_LESSON1_TEMA1")
    return render(request, 'contenidos/unidad2/modulo2-unidad1-lesson1-tm1.html')    

@login_required(login_url="/login-estudiante")
def modulo2_unidad1_lesson1_tm2(request):
    log(request, "CONTENIDO_MODULO2_LESSON1_TEMA2")
    return render(request, 'contenidos/unidad2/modulo2-unidad1-lesson1-tm2.html')

@login_required(login_url="/login-estudiante")
def modulo2_unidad1_lesson1_tm3(request):
    log(request, "CONTENIDO_MODULO2_LESSON1_TEMA3")
    return render(request, 'contenidos/unidad2/modulo2-unidad1-lesson1-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad1_lesson1_tm4(request):
    log(request, "CONTENIDO_MODULO2_LESSON1_TEMA4")
    return render(request, 'contenidos/unidad2/modulo2-unidad1-lesson1-tm4.html')      

@login_required(login_url="/login-estudiante")
def modulo2_unidad1_lesson2_tm1(request):
    log(request, "CONTENIDO_MODULO2_LESSON2_TEMA1")
    return render(request, 'contenidos/unidad2/modulo2-unidad1-lesson2-tm1.html')    

@login_required(login_url="/login-estudiante")
def modulo2_unidad1_lesson2_tm2(request):
    log(request, "CONTENIDO_MODULO2_LESSON2_TEMA2")
    return render(request, 'contenidos/unidad2/modulo2-unidad1-lesson2-tm2.html')

@login_required(login_url="/login-estudiante")
def modulo2_unidad1_lesson2_tm3(request):
    log(request, "CONTENIDO_MODULO2_LESSON2_TEMA3")
    return render(request, 'contenidos/unidad2/modulo2-unidad1-lesson2-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad1_lesson2_tm4(request):
    log(request, "CONTENIDO_MODULO2_LESSON2_TEMA4")
    return render(request, 'contenidos/unidad2/modulo2-unidad1-lesson2-tm4.html')  

@login_required(login_url="/login-estudiante")
def modulo2_unidad1_lesson3_tm1(request):
    log(request, "CONTENIDO_MODULO2_LESSON3_TEMA1")
    return render(request, 'contenidos/unidad2/modulo2-unidad1-lesson3-tm1.html')   

@login_required(login_url="/login-estudiante")
def modulo2_unidad1_lesson3_tm2(request):
    log(request, "CONTENIDO_MODULO2_LESSON3_TEMA2")
    return render(request, 'contenidos/unidad2/modulo2-unidad1-lesson3-tm2.html')

@login_required(login_url="/login-estudiante")
def modulo2_unidad1_lesson3_tm3(request):
    log(request, "CONTENIDO_MODULO2_LESSON3_TEMA3")
    return render(request, 'contenidos/unidad2/modulo2-unidad1-lesson3-tm3.html')   

@login_required(login_url="/login-estudiante")
def modulo2_unidad1_lesson3_tm4(request):
    log(request, "CONTENIDO_MODULO2_LESSON3_TEMA4")
    return render(request, 'contenidos/unidad2/modulo2-unidad1-lesson3-tm4.html')   

@login_required(login_url="/login-estudiante")
def modulo2_unidad2_lesson1_tm1(request):
    log(request, "CONTENIDO_MODULO2_LESSON4_TEMA1")
    return render(request, 'contenidos/unidad2/modulo2-unidad2-lesson1-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad2_lesson1_tm2(request):
    log(request, "CONTENIDO_MODULO2_LESSON4_TEMA2")
    return render(request, 'contenidos/unidad2/modulo2-unidad2-lesson1-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo2_unidad2_lesson1_tm3(request):
    log(request, "CONTENIDO_MODULO2_LESSON4_TEMA3")
    return render(request, 'contenidos/unidad2/modulo2-unidad2-lesson1-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad2_lesson1_tm4(request):
    log(request, "CONTENIDO_MODULO2_LESSON4_TEMA4")
    return render(request, 'contenidos/unidad2/modulo2-unidad2-lesson1-tm4.html')  

@login_required(login_url="/login-estudiante")
def modulo2_unidad2_lesson2_tm1(request):
    log(request, "CONTENIDO_MODULO2_LESSON5_TEMA1")
    return render(request, 'contenidos/unidad2/modulo2-unidad2-lesson2-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad2_lesson2_tm2(request):
    log(request, "CONTENIDO_MODULO2_LESSON5_TEMA2")
    return render(request, 'contenidos/unidad2/modulo2-unidad2-lesson2-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo2_unidad2_lesson2_tm3(request):
    log(request, "CONTENIDO_MODULO2_LESSON5_TEMA3")
    return render(request, 'contenidos/unidad2/modulo2-unidad2-lesson2-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad2_lesson2_tm4(request):
    log(request, "CONTENIDO_MODULO2_LESSON5_TEMA4")
    return render(request, 'contenidos/unidad2/modulo2-unidad2-lesson2-tm4.html')

@login_required(login_url="/login-estudiante")
def modulo2_unidad2_lesson3_tm1(request):
    log(request, "CONTENIDO_MODULO2_LESSON6_TEMA1")
    return render(request, 'contenidos/unidad2/modulo2-unidad2-lesson3-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad2_lesson3_tm2(request):
    log(request, "CONTENIDO_MODULO2_LESSON6_TEMA2")
    return render(request, 'contenidos/unidad2/modulo2-unidad2-lesson3-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo2_unidad2_lesson3_tm3(request):
    log(request, "CONTENIDO_MODULO2_LESSON6_TEMA3")
    return render(request, 'contenidos/unidad2/modulo2-unidad2-lesson3-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad2_lesson3_tm4(request):
    log(request, "CONTENIDO_MODULO2_LESSON6_TEMA4")
    return render(request, 'contenidos/unidad2/modulo2-unidad2-lesson3-tm4.html')   

@login_required(login_url="/login-estudiante")
def modulo2_unidad3_lesson1_tm1(request):
    log(request, "CONTENIDO_MODULO2_LESSON7_TEMA1")
    return render(request, 'contenidos/unidad2/modulo2-unidad3-lesson1-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad3_lesson1_tm2(request):
    log(request, "CONTENIDO_MODULO2_LESSON7_TEMA2")
    return render(request, 'contenidos/unidad2/modulo2-unidad3-lesson1-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo2_unidad3_lesson1_tm3(request):
    log(request, "CONTENIDO_MODULO2_LESSON7_TEMA3")
    return render(request, 'contenidos/unidad2/modulo2-unidad3-lesson1-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad3_lesson1_tm4(request):
    log(request, "CONTENIDO_MODULO2_LESSON7_TEMA4")
    return render(request, 'contenidos/unidad2/modulo2-unidad3-lesson1-tm4.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad3_lesson2_tm1(request):
    log(request, "CONTENIDO_MODULO2_LESSON8_TEMA1")
    return render(request, 'contenidos/unidad2/modulo2-unidad3-lesson2-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad3_lesson2_tm2(request):
    log(request, "CONTENIDO_MODULO2_LESSON8_TEMA2")
    return render(request, 'contenidos/unidad2/modulo2-unidad3-lesson2-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo2_unidad3_lesson2_tm3(request):
    log(request, "CONTENIDO_MODULO2_LESSON8_TEMA3")
    return render(request, 'contenidos/unidad2/modulo2-unidad3-lesson2-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo2_unidad3_lesson2_tm4(request):
    log(request, "CONTENIDO_MODULO2_LESSON8_TEMA4")
    return render(request, 'contenidos/unidad2/modulo2-unidad3-lesson2-tm4.html')

# <---------------------------- modulo 3 ------------------------------------------
@login_required(login_url="/login-estudiante")
def modulo3(request):
    log(request, "CONTENIDO_MODULO3")
    return render(request, 'contenidos/unidad3/modulo3.html')

@login_required(login_url="/login-estudiante")
def modulo3_unidad1(request):
    log(request, "CONTENIDO_MODULO3_UNIDAD1")
    return render(request, 'contenidos/unidad3/modulo3-unidad1.html')

@login_required(login_url="/login-estudiante")
def modulo3_unidad2(request):
    log(request, "CONTENIDO_MODULO3_UNIDAD2")
    return render(request, 'contenidos/unidad3/modulo3-unidad2.html')

@login_required(login_url="/login-estudiante")
def modulo3_unidad3(request):
    log(request, "CONTENIDO_MODULO3_UNIDAD3")
    return render(request, 'contenidos/unidad3/modulo3-unidad3.html')

@login_required(login_url="/login-estudiante")
def modulo3_unidad1_lesson1_tm1(request):
    log(request, "CONTENIDO_MODULO3_LESSON1_TEMA1")
    return render(request, 'contenidos/unidad3/modulo3-unidad1-lesson1-tm1.html')    

@login_required(login_url="/login-estudiante")
def modulo3_unidad1_lesson1_tm2(request):
    log(request, "CONTENIDO_MODULO3_LESSON1_TEMA2")
    return render(request, 'contenidos/unidad3/modulo3-unidad1-lesson1-tm2.html')

@login_required(login_url="/login-estudiante")
def modulo3_unidad1_lesson1_tm3(request):
    log(request, "CONTENIDO_MODULO3_LESSON1_TEMA3")
    return render(request, 'contenidos/unidad3/modulo3-unidad1-lesson1-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad1_lesson1_tm4(request):
    log(request, "CONTENIDO_MODULO3_LESSON1_TEMA4")
    return render(request, 'contenidos/unidad3/modulo3-unidad1-lesson1-tm4.html')      

@login_required(login_url="/login-estudiante")
def modulo3_unidad1_lesson2_tm1(request):
    log(request, "CONTENIDO_MODULO3_LESSON2_TEMA1")
    return render(request, 'contenidos/unidad3/modulo3-unidad1-lesson2-tm1.html')    

@login_required(login_url="/login-estudiante")
def modulo3_unidad1_lesson2_tm2(request):
    log(request, "CONTENIDO_MODULO3_LESSON2_TEMA2")
    return render(request, 'contenidos/unidad3/modulo3-unidad1-lesson2-tm2.html')

@login_required(login_url="/login-estudiante")
def modulo3_unidad1_lesson2_tm3(request):
    log(request, "CONTENIDO_MODULO3_LESSON2_TEMA3")
    return render(request, 'contenidos/unidad3/modulo3-unidad1-lesson2-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad1_lesson2_tm4(request):
    log(request, "CONTENIDO_MODULO3_LESSON2_TEMA4")
    return render(request, 'contenidos/unidad3/modulo3-unidad1-lesson2-tm4.html')  

@login_required(login_url="/login-estudiante")
def modulo3_unidad1_lesson3_tm1(request):
    log(request, "CONTENIDO_MODULO3_LESSON3_TEMA1")
    return render(request, 'contenidos/unidad3/modulo3-unidad1-lesson3-tm1.html')   

@login_required(login_url="/login-estudiante")
def modulo3_unidad1_lesson3_tm2(request):
    log(request, "CONTENIDO_MODULO3_LESSON3_TEMA2")
    return render(request, 'contenidos/unidad3/modulo3-unidad1-lesson3-tm2.html')

@login_required(login_url="/login-estudiante")
def modulo3_unidad1_lesson3_tm3(request):
    log(request, "CONTENIDO_MODULO3_LESSON3_TEMA3")
    return render(request, 'contenidos/unidad3/modulo3-unidad1-lesson3-tm3.html')   

@login_required(login_url="/login-estudiante")
def modulo3_unidad1_lesson3_tm4(request):
    log(request, "CONTENIDO_MODULO3_LESSON3_TEMA4")
    return render(request, 'contenidos/unidad3/modulo3-unidad1-lesson3-tm4.html')   

@login_required(login_url="/login-estudiante")
def modulo3_unidad2_lesson1_tm1(request):
    log(request, "CONTENIDO_MODULO3_LESSON4_TEMA1")
    return render(request, 'contenidos/unidad3/modulo3-unidad2-lesson1-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad2_lesson1_tm2(request):
    log(request, "CONTENIDO_MODULO3_LESSON4_TEMA2")
    return render(request, 'contenidos/unidad3/modulo3-unidad2-lesson1-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo3_unidad2_lesson1_tm3(request):
    log(request, "CONTENIDO_MODULO3_LESSON4_TEMA3")
    return render(request, 'contenidos/unidad3/modulo3-unidad2-lesson1-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad2_lesson1_tm4(request):
    log(request, "CONTENIDO_MODULO3_LESSON4_TEMA4")
    return render(request, 'contenidos/unidad3/modulo3-unidad2-lesson1-tm4.html')  

@login_required(login_url="/login-estudiante")
def modulo3_unidad2_lesson2_tm1(request):
    log(request, "CONTENIDO_MODULO3_LESSON5_TEMA1")
    return render(request, 'contenidos/unidad3/modulo3-unidad2-lesson2-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad2_lesson2_tm2(request):
    log(request, "CONTENIDO_MODULO3_LESSON5_TEMA2")
    return render(request, 'contenidos/unidad3/modulo3-unidad2-lesson2-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo3_unidad2_lesson2_tm3(request):
    log(request, "CONTENIDO_MODULO3_LESSON5_TEMA3")
    return render(request, 'contenidos/unidad3/modulo3-unidad2-lesson2-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad2_lesson2_tm4(request):
    log(request, "CONTENIDO_MODULO3_LESSON5_TEMA4")
    return render(request, 'contenidos/unidad3/modulo3-unidad2-lesson2-tm4.html')

@login_required(login_url="/login-estudiante")
def modulo3_unidad2_lesson3_tm1(request):
    log(request, "CONTENIDO_MODULO3_LESSON6_TEMA1")
    return render(request, 'contenidos/unidad3/modulo3-unidad2-lesson3-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad2_lesson3_tm2(request):
    log(request, "CONTENIDO_MODULO3_LESSON6_TEMA2")
    return render(request, 'contenidos/unidad3/modulo3-unidad2-lesson3-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo3_unidad2_lesson3_tm3(request):
    log(request, "CONTENIDO_MODULO3_LESSON6_TEMA3")
    return render(request, 'contenidos/unidad3/modulo3-unidad2-lesson3-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad2_lesson3_tm4(request):
    log(request, "CONTENIDO_MODULO3_LESSON6_TEMA4")
    return render(request, 'contenidos/unidad3/modulo3-unidad2-lesson3-tm4.html')   

@login_required(login_url="/login-estudiante")
def modulo3_unidad3_lesson1_tm1(request):
    log(request, "CONTENIDO_MODULO3_LESSON7_TEMA1")
    return render(request, 'contenidos/unidad3/modulo3-unidad3-lesson1-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad3_lesson1_tm2(request):
    log(request, "CONTENIDO_MODULO3_LESSON7_TEMA2")
    return render(request, 'contenidos/unidad3/modulo3-unidad3-lesson1-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo3_unidad3_lesson1_tm3(request):
    log(request, "CONTENIDO_MODULO3_LESSON7_TEMA3")
    return render(request, 'contenidos/unidad3/modulo3-unidad3-lesson1-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad3_lesson1_tm4(request):
    log(request, "CONTENIDO_MODULO3_LESSON7_TEMA4")
    return render(request, 'contenidos/unidad3/modulo3-unidad3-lesson1-tm4.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad3_lesson2_tm1(request):
    log(request, "CONTENIDO_MODULO3_LESSON8_TEMA1")
    return render(request, 'contenidos/unidad3/modulo3-unidad3-lesson2-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad3_lesson2_tm2(request):
    log(request, "CONTENIDO_MODULO3_LESSON8_TEMA2")
    return render(request, 'contenidos/unidad3/modulo3-unidad3-lesson2-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo3_unidad3_lesson2_tm3(request):
    log(request, "CONTENIDO_MODULO3_LESSON8_TEMA3")
    return render(request, 'contenidos/unidad3/modulo3-unidad3-lesson2-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo3_unidad3_lesson2_tm4(request):
    log(request, "CONTENIDO_MODULO3_LESSON8_TEMA4")
    return render(request, 'contenidos/unidad3/modulo3-unidad3-lesson2-tm4.html')  

# <---------------------------- modulo 4 ------------------------------------------
@login_required(login_url="/login-estudiante")
def modulo4(request):
    log(request, "CONTENIDO_MODULO4")
    return render(request, 'contenidos/unidad4/modulo4.html')

@login_required(login_url="/login-estudiante")
def modulo4_unidad1(request):
    log(request, "CONTENIDO_MODULO4_UNIDAD1")
    return render(request, 'contenidos/unidad4/modulo4-unidad1.html')

@login_required(login_url="/login-estudiante")
def modulo4_unidad2(request):
    log(request, "CONTENIDO_MODULO4_UNIDAD2")
    return render(request, 'contenidos/unidad4/modulo4-unidad2.html')

@login_required(login_url="/login-estudiante")
def modulo4_unidad3(request):
    log(request, "CONTENIDO_MODULO4_UNIDAD3")
    return render(request, 'contenidos/unidad4/modulo4-unidad3.html')

@login_required(login_url="/login-estudiante")
def modulo4_unidad1_lesson1_tm1(request):
    log(request, "CONTENIDO_MODULO4_LESSON1_TEMA1")
    return render(request, 'contenidos/unidad4/modulo4-unidad1-lesson1-tm1.html')    

@login_required(login_url="/login-estudiante")
def modulo4_unidad1_lesson1_tm2(request):
    log(request, "CONTENIDO_MODULO4_LESSON1_TEMA2")
    return render(request, 'contenidos/unidad4/modulo4-unidad1-lesson1-tm2.html')

@login_required(login_url="/login-estudiante")
def modulo4_unidad1_lesson1_tm3(request):
    log(request, "CONTENIDO_MODULO4_LESSON1_TEMA3")
    return render(request, 'contenidos/unidad4/modulo4-unidad1-lesson1-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad1_lesson1_tm4(request):
    log(request, "CONTENIDO_MODULO4_LESSON1_TEMA4")
    return render(request, 'contenidos/unidad4/modulo4-unidad1-lesson1-tm4.html')      

@login_required(login_url="/login-estudiante")
def modulo4_unidad1_lesson2_tm1(request):
    log(request, "CONTENIDO_MODULO4_LESSON2_TEMA1")
    return render(request, 'contenidos/unidad4/modulo4-unidad1-lesson2-tm1.html')    

@login_required(login_url="/login-estudiante")
def modulo4_unidad1_lesson2_tm2(request):
    log(request, "CONTENIDO_MODULO4_LESSON2_TEMA2")
    return render(request, 'contenidos/unidad4/modulo4-unidad1-lesson2-tm2.html')

@login_required(login_url="/login-estudiante")
def modulo4_unidad1_lesson2_tm3(request):
    log(request, "CONTENIDO_MODULO4_LESSON2_TEMA3")
    return render(request, 'contenidos/unidad4/modulo4-unidad1-lesson2-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad1_lesson2_tm4(request):
    log(request, "CONTENIDO_MODULO4_LESSON2_TEMA4")
    return render(request, 'contenidos/unidad4/modulo4-unidad1-lesson2-tm4.html')  

@login_required(login_url="/login-estudiante")
def modulo4_unidad1_lesson3_tm1(request):
    log(request, "CONTENIDO_MODULO4_LESSON3_TEMA1")
    return render(request, 'contenidos/unidad4/modulo4-unidad1-lesson3-tm1.html')   

@login_required(login_url="/login-estudiante")
def modulo4_unidad1_lesson3_tm2(request):
    log(request, "CONTENIDO_MODULO4_LESSON3_TEMA2")
    return render(request, 'contenidos/unidad4/modulo4-unidad1-lesson3-tm2.html')

@login_required(login_url="/login-estudiante")
def modulo4_unidad1_lesson3_tm3(request):
    log(request, "CONTENIDO_MODULO4_LESSON3_TEMA3")
    return render(request, 'contenidos/unidad4/modulo4-unidad1-lesson3-tm3.html')   

@login_required(login_url="/login-estudiante")
def modulo4_unidad1_lesson3_tm4(request):
    log(request, "CONTENIDO_MODULO4_LESSON3_TEMA4")
    return render(request, 'contenidos/unidad4/modulo4-unidad1-lesson3-tm4.html')   

@login_required(login_url="/login-estudiante")
def modulo4_unidad2_lesson1_tm1(request):
    log(request, "CONTENIDO_MODULO4_LESSON4_TEMA1")
    return render(request, 'contenidos/unidad4/modulo4-unidad2-lesson1-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad2_lesson1_tm2(request):
    log(request, "CONTENIDO_MODULO4_LESSON4_TEMA2")
    return render(request, 'contenidos/unidad4/modulo4-unidad2-lesson1-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo4_unidad2_lesson1_tm3(request):
    log(request, "CONTENIDO_MODULO4_LESSON4_TEMA3")
    return render(request, 'contenidos/unidad4/modulo4-unidad2-lesson1-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad2_lesson1_tm4(request):
    log(request, "CONTENIDO_MODULO4_LESSON4_TEMA4")
    return render(request, 'contenidos/unidad4/modulo4-unidad2-lesson1-tm4.html')  

@login_required(login_url="/login-estudiante")
def modulo4_unidad2_lesson2_tm1(request):
    log(request, "CONTENIDO_MODULO4_LESSON5_TEMA1")
    return render(request, 'contenidos/unidad4/modulo4-unidad2-lesson2-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad2_lesson2_tm2(request):
    log(request, "CONTENIDO_MODULO4_LESSON5_TEMA2")
    return render(request, 'contenidos/unidad4/modulo4-unidad2-lesson2-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo4_unidad2_lesson2_tm3(request):
    log(request, "CONTENIDO_MODULO4_LESSON5_TEMA3")
    return render(request, 'contenidos/unidad4/modulo4-unidad2-lesson2-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad2_lesson2_tm4(request):
    log(request, "CONTENIDO_MODULO4_LESSON5_TEMA4")
    return render(request, 'contenidos/unidad4/modulo4-unidad2-lesson2-tm4.html')

@login_required(login_url="/login-estudiante")
def modulo4_unidad2_lesson3_tm1(request):
    log(request, "CONTENIDO_MODULO4_LESSON6_TEMA1")
    return render(request, 'contenidos/unidad4/modulo4-unidad2-lesson3-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad2_lesson3_tm2(request):
    log(request, "CONTENIDO_MODULO4_LESSON6_TEMA2")
    return render(request, 'contenidos/unidad4/modulo4-unidad2-lesson3-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo4_unidad2_lesson3_tm3(request):
    log(request, "CONTENIDO_MODULO4_LESSON6_TEMA3")
    return render(request, 'contenidos/unidad4/modulo4-unidad2-lesson3-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad2_lesson3_tm4(request):
    log(request, "CONTENIDO_MODULO4_LESSON6_TEMA4")
    return render(request, 'contenidos/unidad4/modulo4-unidad2-lesson3-tm4.html')   

@login_required(login_url="/login-estudiante")
def modulo4_unidad3_lesson1_tm1(request):
    log(request, "CONTENIDO_MODULO4_LESSON7_TEMA1")
    return render(request, 'contenidos/unidad4/modulo4-unidad3-lesson1-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad3_lesson1_tm2(request):
    log(request, "CONTENIDO_MODULO4_LESSON7_TEMA2")
    return render(request, 'contenidos/unidad4/modulo4-unidad3-lesson1-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo4_unidad3_lesson1_tm3(request):
    log(request, "CONTENIDO_MODULO4_LESSON7_TEMA3")
    return render(request, 'contenidos/unidad4/modulo4-unidad3-lesson1-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad3_lesson1_tm4(request):
    log(request, "CONTENIDO_MODULO4_LESSON7_TEMA4")
    return render(request, 'contenidos/unidad4/modulo4-unidad3-lesson1-tm4.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad3_lesson2_tm1(request):
    log(request, "CONTENIDO_MODULO4_LESSON8_TEMA1")
    return render(request, 'contenidos/unidad4/modulo4-unidad3-lesson2-tm1.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad3_lesson2_tm2(request):
    log(request, "CONTENIDO_MODULO4_LESSON8_TEMA2")
    return render(request, 'contenidos/unidad4/modulo4-unidad3-lesson2-tm2.html')    

@login_required(login_url="/login-estudiante")
def modulo4_unidad3_lesson2_tm3(request):
    log(request, "CONTENIDO_MODULO4_LESSON8_TEMA3")
    return render(request, 'contenidos/unidad4/modulo4-unidad3-lesson2-tm3.html') 

@login_required(login_url="/login-estudiante")
def modulo4_unidad3_lesson2_tm4(request):
    log(request, "CONTENIDO_MODULO4_LESSON8_TEMA4")
    return render(request, 'contenidos/unidad4/modulo4-unidad3-lesson2-tm4.html') 

# <---------------------------- Profes ----------------------------->
@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def inicio_profesor(request):
    usuario = Profesor.objects.get(id=request.user.id)
    return render(request, 'paginaDocente/inicio-profe.html', { 'usuario': usuario } )

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def primer_modulo(request):
    estudiantes = Estudiante.objects.filter()
    return render(request, 'paginaDocente/primer-modulo.html', {'estudiantes': estudiantes})

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def grupos_estudiantes(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    estudiantes = Grupo_Estudiante.objects.filter(grupo_id=pk)
    return render(request, 'paginaDocente/primer-modulo-estudiantes.html', {'estudiantes': estudiantes, 'grupo':grupo} )

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def notas(request):
    user = User.objects.get(id=request.user.id)
    profe = Profesor.objects.get(id=user)
    curso = Curso.objects.get(Profesor_id=profe)
    grupos = Grupo.objects.filter(Curso_id=curso)
    return render(request, 'paginaDocente/notas.html', { 'grupos':grupos })

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def notas_est(request, pk):
    grupo = Grupo.objects.filter(pk=pk)
    estudiantes = Grupo_Estudiante.objects.filter(grupo_id=pk)
    
    data = []
    for e in estudiantes:
        uni = {}
        uni['id'] = e.estudiante.id.id
        uni['nombre'] = e.estudiante.id.first_name
        uni['documento'] = e.estudiante.documento

        data.append(uni)

    res = json.dumps(data)

    return HttpResponse(res)

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def registro_estudiante(request):
    user = User.objects.get(id=request.user.id)
    profe = Profesor.objects.get(id=user)
    curso = Curso.objects.get(Profesor_id=profe)
    grupos = Grupo.objects.filter(Curso_id=curso)

    error = False
    if request.method == 'POST':
        validators = FormRegistroValidator(request.POST)
        validators.required = ['nombre', 'apellidos', 'email', 'documento', 'sexo', 'username', 'password1', 'curso', 'grupo']

        # import pdb; pdb.set_trace()
        if validators.is_valid():
            usuario = User()
            usuario.first_name = request.POST['nombre']
            usuario.last_name = request.POST['apellidos']
            usuario.email = request.POST['email']
            usuario.username = request.POST['username']
            usuario.password = make_password(request.POST['password1'])
            usuario.is_active = True
            perfil = Group.objects.get(name="Estudiantes")  # carga un perfil de tipo usuario
            usuario.save()
            usuario.groups.add(perfil)
            usuario.save()

            myusuario = Estudiante()
            myusuario.id = usuario
            myusuario.documento = request.POST['documento']
            myusuario.sexo = request.POST['sexo']
            myusuario.save()


            grupoestudiante = Grupo_Estudiante()
            grupoestudiante.estudiante = myusuario
            grupoestudiante.curso_id = request.POST.get('curso')
            grupoestudiante.grupo_id = request.POST.get('grupo')            
            grupoestudiante.save()

            #TODO: ENviar correo electronico para confirmar cuenta
            asunto = "Registro en English Easy"
            body = render_to_string('email.html', {'user': usuario})

            #send_mail(asunto, body, EMAIL_HOST_USER, [ usuario.email ] )
            # msg = EmailMultiAlternatives(asunto, body, EMAIL_HOST_USER, [usuario.email])
            # msg.content_subtype = "html"
            # msg.send()

            return render(request, 'paginaDocente/registro-estudiante.html', {'success': True, 'grupos':grupos} )
        else:
            return render(request, 'paginaDocente/registro-estudiante.html', {'error': validators.getMessage(), 'grupos':grupos } )
        # Agregar el usuario a la base de datos
    return render(request, 'paginaDocente/registro-estudiante.html', {'grupos':grupos} )

def buscar_estudiante(request):
    estudiante = None
    buscar = None
    if 'buscar' in request.GET.keys():
        buscar = request.GET['identificacion']
        qset = (Q(documento__icontains=buscar) )
        estudiante = Estudiante.objects.filter(qset).distinct()

    return render(request, 'paginaDocente/registro-estudiante.html', {'estudiante': estudiante, 'filtro': buscar} )

def buscar_estudiante1(request):

    estudiante = None
    buscar = None
    if 'buscar' in request.GET.keys():
        buscar = request.GET['identificacion']
        qset = (Q(documento__icontains=buscar) )
        estudiante = Estudiante.objects.filter(qset).first()

    return render(request, 'paginaDocente/eliminar-estudiante.html', {'estudiante': estudiante, 'filtro': buscar} )

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def perfil_profesor(request):
    usuario = Profesor.objects.get(id=request.user.id)
    return render(request, 'paginaDocente/perfil-profe.html', { 'usuario': usuario })

def modificar_perfil(request):
    error = False
    if request.method == 'POST':
        usu = User.objects.get( id = request.user.id )
        usu.email = request.POST['email']
        usu.save()

        miusuario = Profesor()
        miusuario.id = usu
        miusuario.cedula = request.POST['cedula']
        miusuario.profesion = request.POST['profesion']
        miusuario.especialidad = request.POST['especialidad']
        miusuario.save()

    return render(request, 'paginaDocente/perfil-profe.html', { "usuario": usu } )

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def modificar_contra_profesor(request):
    error = False
    usu1 = None
    if request.method == 'POST':
        usu1 = User.objects.get(id=request.user.id)
        usu1.password = make_password(request.POST['password1'])
        usu1.save()

    return render(request, 'paginaDocente/perfil-profe.html', { 'usuario': usu1 } )

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def eliminar_estudiante(request):

    return render(request, 'paginaDocente/eliminar-estudiante.html' )

import simplejson
@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def elimina_est(request, pk):

    pks = request.POST.get('id')
    estudiante = User.objects.get(pk=pks)
    estudiante.delete()
    return redirect('eliminar-estudiante')

# <------------------------------- Grupos ------------------------------------->

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def lista_grupos(request):
    user = User.objects.get(id=request.user.id)
    profe = Profesor.objects.get(id=user)
    curso = Curso.objects.get(Profesor_id=profe)
    grupos = Grupo.objects.filter(Curso_id=curso)
    return render(request, 'paginaDocente/grupos.html', {'grupos':grupos }  )

# Función Crear Grupos
@method_decorator(login_required(login_url="/login-profesor"), name='dispatch')
# @method_decorator(restringir_estudiante, name='dispatch')
class createGrupos(CreateView):
    model = Grupo # Importa el modelo
    form_class = GrupoForm # Importa el form del modelo
    template_name = 'paginaDocente/agregar-grupos.html' # Importa el template
    success_url=reverse_lazy('lista-grupos') # como se va a retornar

    def get_form_kwargs(self, **kwargs): # Función para agregar variables Externas al form
        form_kwargs = super(createGrupos, self).get_form_kwargs(**kwargs) # Llama a la clase principal, siempre debe ir
        form_kwargs["user"] = self.request.user
        return form_kwargs

@method_decorator(login_required(login_url="/login-profesor"), name='dispatch')
# @method_decorator(restringir_estudiante, name='dispatch')
class editGrupos(UpdateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'paginaDocente/edit-grupos.html'
    success_url=reverse_lazy('lista-grupos')

@method_decorator(login_required(login_url="/login-profesor"), name='dispatch')
# @method_decorator(restringir_estudiante, name='dispatch')
class deleteGrupos(DeleteView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'paginaDocente/delete-grupos.html'
    success_url=reverse_lazy('lista-grupos')

# <------------------------------ Cursos -------------------------------------->

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def lista_curso(request):
    curso = Curso.objects.filter(Profesor_id=request.user.id)
    return render(request, 'paginaDocente/curso.html', {'curso':curso} )

# Función Crear Cursos
@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def agregar_curso(request):
    # almacena el usuario logeado
    usu = request.user
    if request.method == "POST":
        # se importa la funcion de forms.py correspondiente a la tabla
        # la variable form toma los datos ingresados por el usuario
        form = CursoForm(request.POST)
        # se validan si los datos ingresados son correctos
        if form.is_valid():
            # si son correctos, entonces la variable curso toma
            # los valores que tenia form, con el 'commit=False'
            # se hace una pausa antes de guardar los datos
            curso = form.save(commit=False)
            # el campo 'Profesor_id' toma el valor del usuario logeado
            curso.Profesor_id = usu.id
            # se guardan los cambios
            curso.save()
            # se redirige a la vista indicada
            return redirect('lista-curso')
    else:
        form = CursoForm()
    return render(request, 'paginaDocente/agregar-curso.html', {'form': form, 'usu':usu} )

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.Profesor_id = request.user.id
            curso.save()
            return redirect('lista-curso')
    else:
        form = CursoForm(instance=curso)

    return render(request, 'paginaDocente/editar-curso.html', {'form': form})

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect('lista-curso')

# <------------------------------ Calificacion -------------------------------------->

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def lista_notas(request, pk):
    # import pdb; pdb.set_trace()
    estudiante = User.objects.get(id=pk)
    grupos_estudiantes = Grupo_Estudiante.objects.get(estudiante_id=pk)
    notas = Calificacion.objects.filter(grupo_estudiante=grupos_estudiantes)
    p = 0
    e = 0
    t = 0
    for i in notas:
        if (i.nota >= 0 and i.nota <= 2.9):
            p=p+1
        if (i.nota >= 3.0 and i.nota <= 3.9):
            e=e+1
        if (i.nota >= 4.0 and i.nota <= 5):
            t=t+1

    return render(request, 'paginaDocente/lista-notas.html', {'notas':notas, 'estudiante':estudiante, "p":p, "e":e, "t":t} )

# Función Agregar Notas
@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def agregar_notas(request, pk):
    # import pdb; pdb.set_trace()
    estudiante = User.objects.get(id=pk)
    actividad = Actividades.objects.all()
    grupos_estudiantes = Grupo_Estudiante.objects.get(estudiante_id=pk)
    if request.method == "POST":
        notas = Calificacion()
        notas.nota = request.POST['nota']
        notas.detalle = request.POST['detalle']
        notas.actividad_id = request.POST.get('actividad', None )
        notas.grupo_estudiante_id = grupos_estudiantes.id
        notas.save()
        return redirect('lista-notas', pk=pk)

    return render(request, 'paginaDocente/agregar-notas.html', {'estudiante':estudiante, 'actividad':actividad} )

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def editar_notas(request, pk):
    # import pdb; pdb.set_trace()
    notas = Calificacion.objects.filter(pk=pk)
    if request.method == "POST":
        notas = Calificacion()
        nota = request.POST['nota']
        notas.nota = float(nota)
        notas.detalle = request.POST['detalle']
        # notas.actividad_id = request.POST.get('actividad', None )
        notas.grupo_estudiante_id = request.POST['grupo']
        notas.save()
        return redirect('lista-grupos')

    return render(request, 'paginaDocente/edit-notas.html', {'notas':notas })

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def eliminar_notas(request, pk):
    notas = get_object_or_404(Calificacion, pk=pk)
    notas.delete()
    return redirect('lista-grupos')

# def reporte_notas(request, pk):

#     return render(request,'../templates/index.html', { "user": user, "p":p, "e":e, "t":t} )

# <----------------------------------- Eventos --------------------------------->
@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def eventos_estudiantes(request, pk):
    log = Log.objects.filter(usuario=pk)
    user = User.objects.get(pk=pk)
    return render(request, 'paginaDocente/eventos-estudiantes.html', {'eventos':log, 'user':user} )

# <----------------------------------- Funciones ------------------------------->
import xhtml2pdf.pisa as pisa
from StringIO import StringIO
from django.template.loader import render_to_string
def pdf(f):
    def funcion(*args, **kwargs):
        html = f(*args, **kwargs)
        result = StringIO() #creamos una instancia del un objeto StringIO para
        pdf = pisa.pisaDocument( html , result) # convertimos en pdf la template
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return funcion

@pdf
def reporte_estudiante(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    estudiantes = Grupo_Estudiante.objects.filter(grupo_id=pk)
    return render_to_string("paginaDocente/reporte_estudiantes.html", { 'estudiantes': estudiantes, }) #obtenemos la plantilla


def log(request, action):
    log = Log()
    log.usuario = request.user.id
    if (Estudiante.objects.filter(id=request.user.id).exists()):
        log.tipo = 'E'
    elif (Profesor.objects.filter(id=request.user.id).exists()):
        log.tipo = 'P'
    else:
        log.tipo = 'A'
    log.accion = action
    log.save() 

def guarda_actividad(request, pk):
    estudiante = User.objects.get(id=pk)
    grupos_estudiantes = Grupo_Estudiante.objects.get(estudiante_id=pk)
    if request.method == "POST":
        notas = Calificacion()
        notas.nota = request.POST.get('nota')
        notas.detalle = request.POST.get('detalle')
        notas.actividad_id = request.POST.get('actividad')
        notas.grupo_estudiante_id = grupos_estudiantes.id
        notas.save()
        return HttpResponse('Bien')
