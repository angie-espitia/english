# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from .validator import FormRegistroValidator, FormLoginValidator


def index(request):
    return render_to_response('index.html')

def curso(request):
    return render_to_response('../templates/curso.html')

def login_estudiante(request):

    if request.method == 'POST':

        validators = FormLoginValidator(request.POST)

        if validators.is_valid():

            usuario = request.POST['usuario']
            clave = request.POST['clave']
            auth.login(request, validators.acceso)  # Crear una sesion
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
            return HttpResponseRedirect('/inicio-profesor')

        else:
            return render_to_response('../templates/login-profe.html', {'error': validator.getMessage()} , context_instance = RequestContext(request))

    return render_to_response('../templates/login-profe.html', context_instance=RequestContext(request))

@login_required(login_url="/login-estudiante")
def inicio_estudiante(request):
    return render_to_response('inicio-estudiante.html')

@login_required(login_url="/login-estudiante")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")



@login_required(login_url="/login-estudiante")
def modulo1(request):
    return render_to_response('../templates/modulo1.html')

@login_required(login_url="/login-estudiante")
def modulo1_unidad1(request):
    return render_to_response('../templates/modulo1-unidad1.html')

@login_required(login_url="/login-estudiante")
def unidad1_tm1(request):
    return render_to_response('../templates/modulo1-unidad1 -tm1.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson1_tm2(request):
    return render_to_response('../templates/modulo1-unidad1-lesson1-tm2.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson1_tm3(request):
    return render_to_response('../templates/modulo1-unidad1-lesson1-tm3.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson1_tm4(request):
    return render_to_response('../templates/modulo1-unidad1-lesson1-tm4.html')



@login_required(login_url="/login-profesor")
def inicio_profesor(request):
    return render_to_response('../templates/inicio-profe.html')

@login_required(login_url="/login-profesor")
def primer_modulo(request):
    return render_to_response('../templates/primer-modulo.html')

from django.contrib.auth.hashers import make_password
from .models import Estudiante
@login_required(login_url="/login-profesor")
def registro_estudiante(request):
    """view del profile
    """
    error = False
    if request.method == 'POST':
        validators = FormRegistroValidator(request.POST)
        validators.required = ['nombre', 'apellidos', 'documento', 'username', 'email', 'password1']

        if validators.is_valid():
            usuario = Estudiante()
            usuario.nombre = request.POST['nombre']
            usuario.apellido = request.POST['apellidos']
            usuario.cedula = request.POST['documento']
            usuario.username = request.POST['username']
            usuario.email = request.POST['email']
            usuario.clave = make_password(request.POST['password1'])
            #TODO: ENviar correo electronico para confirmar cuenta
            usuario.is_active = True
            usuario.save()
            return render_to_response('../templates/registro-estudiante.html', {'success': True}, context_instance=RequestContext(request))
        else:
            return render_to_response('../templates/registro-estudiante.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
        # Agregar el usuario a la base de datos
    return render_to_response('../templates/registro-estudiante.html', context_instance = RequestContext(request))