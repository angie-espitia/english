# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from .validator import FormRegistroValidator, FormLoginValidator
from english.settings import STATIC_ROLS


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

def restringir_estudiante(User):
     if User.groups.filter(id = STATIC_ROLS['Estudiantes']).exists():
         return False
     return True

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

@login_required(login_url="/login-estudiante")
def unidad1_lesson2_tm1(request):
    return render_to_response('../templates/modulo1-unidad1-lesson2-tm1.html')


@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def inicio_profesor(request):
    return render_to_response('../templates/inicio-profe.html')

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def primer_modulo(request):
    return render_to_response('../templates/primer-modulo.html')

from django.contrib.auth.hashers import make_password
from .models import Estudiante
@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def registro_estudiante(request):
    """view del profile
    """
    error = False
    if request.method == 'POST':
        validators = FormRegistroValidator(request.POST)
        validators.required = ['nombre', 'apellidos', 'email', 'cedula', 'username', 'password1']

        if validators.is_valid():
            usuario = User()
            usuario.first_name = request.POST['nombre']
            usuario.last_name = request.POST['apellidos']
            usuario.email = request.POST['email']
            usuario.cedula = request.POST['cedula']
            usuario.username = request.POST['username']
            usuario.password = make_password(request.POST['password1'])
            usuario.is_active = True
            perfil = Group.objects.get(name="Estudiantes")  # carga un perfil de tipo usuario
            usuario.save()
            usuario.groups.add(perfil)
            usuario.save()

            myusuario = Estudiante()
            myusuario.id = usuario
            myusuario.sexo = request.POST['sexo']
            myusuario.save()

            return render_to_response('../templates/registro-estudiante.html', {'success': True}, context_instance=RequestContext(request))
        else:
            return render_to_response('../templates/registro-estudiante.html', {'error': validators.getMessage() } , context_instance = RequestContext(request))
        # Agregar el usuario a la base de datos
    return render_to_response('../templates/registro-estudiante.html', context_instance = RequestContext(request))

from django.db.models import Q
def buscar_estudiante(request):

    estudiante = None
    buscar = None
    if 'buscar' in request.GET.keys():
        buscar = request.GET['buscar']
        qset = (Q(username__icontains=buscar) )
        estudiante = User.objects.filter(qset)

    return render_to_response('registro-estudiante.html', {'cursos': estudiante, 'filtro': buscar},
                              context_instance=RequestContext(request))