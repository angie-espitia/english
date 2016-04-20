# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.exceptions import NON_FIELD_ERRORS
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from project.forms import LoginForm


def index(request):
    return render_to_response('index.html')

def curso(request):
    return render_to_response('../templates/curso.html')

def login_estudiante(request):
    """view del login
    """
    #Verificamos que los datos lleguen por el methodo POST
    formulario = LoginForm()
    if request.method == 'POST':
        #Cargamos el formulario (ver forms.py con los datos del POST)
        formulario = LoginForm(data = request.POST)
        #Verificamos que los datos esten correctos segun su estructura
        if formulario.is_valid():
            # Capturamos las variables que llegan por POST
            usuario = request.POST.get('usuario')
            clave = request.POST.get('clave')

            #validamos los datos de usuario y contraseña, el metodo authenticate verifica el password cifrado
            acceso = auth.authenticate(username = usuario, password = clave )
            #Si el usuario existe abrimos una sesion de usuario

            if not acceso is None:
                auth.login(request, acceso)
                return HttpResponseRedirect('/inicio')
            else:
                formulario._errors = { NON_FIELD_ERRORS:  'Usuario o Password Invalido'}


    return render_to_response('../templates/login-estudiante.html', {"form": formulario} , context_instance = RequestContext(request))

def login_profesor(request):
    """view del login
    """
    #Verificamos que los datos lleguen por el methodo POST
    formulario = LoginForm()
    if request.method == 'POST':
        #Cargamos el formulario (ver forms.py con los datos del POST)
        formulario = LoginForm(data = request.POST)
        #Verificamos que los datos esten correctos segun su estructura
        if formulario.is_valid():
            # Capturamos las variables que llegan por POST
            usuario = request.POST.get('usuario')
            clave = request.POST.get('clave')

            #validamos los datos de usuario y contraseña, el metodo authenticate verifica el password cifrado
            acceso = auth.authenticate(username = usuario, password = clave )
            #Si el usuario existe abrimos una sesion de usuario

            if not acceso is None:
                auth.login(request, acceso)
                return HttpResponseRedirect('/inicio-profesor')
            else:
                formulario._errors = { NON_FIELD_ERRORS:  'Usuario o Password Invalido'}


    return render_to_response('../templates/login-profe.html', {"form": formulario} , context_instance = RequestContext(request))

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

@login_required(login_url="/login-profesor")
def inicio_profesor(request):
    return render_to_response('../templates/inicio-profe.html')

@login_required(login_url="/login-profesor")
def primer_modulo(request):
    return render_to_response('../templates/primer-modulo.html')

from django.contrib.auth.hashers import make_password
from .models import Estudiante
from validator import Validator
@login_required(login_url="/login-profesor")
def registro_estudiante(request):
    """view del profile
    """
    error = False
    if request.method == 'POST':
        validator = Validator(request.POST)
        validator.required = ['nombre', 'apellidos', 'email']

        if validator.is_valid():
            usuario = Estudiante()
            #p = Persona.objects.get(documento = '123123123321')
            usuario.first_name = request.POST['nombre']
            usuario.last_name = request.POST['apellidos']
            usuario.username = request.POST['email']
            usuario.password = make_password(request.POST['password1'])
            #TODO: ENviar correo electronico para confirmar cuenta
            usuario.is_active = True
            usuario.save()
        else:
            return render_to_response('../templates/registro-estudiante.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
        # Agregar el usuario a la base de datos
    return render_to_response('../templates/registro-estudiante.html', context_instance = RequestContext(request))