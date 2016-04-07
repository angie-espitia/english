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
    return render_to_response('../templates/login-profe.html')

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

def Registro(request):

    if request.method == 'POST':
        usuario = Usuario()
        usuario.nombre = request.POST('nombre')
        usuario.apellido = request.POST('apellido')
        usuario.username = request.POST('email')
        usuario.clave = request.POST('password')
        usuario.sexo = request.POST('sexo')
        usuario.cedula = request.POST('cedula')

    Usuario_is_active = True
    Usuario.save()