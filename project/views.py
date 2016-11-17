# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import auth
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from .validator import FormRegistroValidator, FormLoginValidator
from english.settings import STATIC_ROLS, EMAIL_HOST_USER
from .models import Estudiante, Profesor


def index(request):
    return render_to_response('index.html')

def curso(request):
    return render_to_response('../templates/curso.html')

def contacto(request):
    return render_to_response('../templates/contacto.html')

def contacto_f(request):
    return render_to_response('../templates/contacto-f')

def login_estudiante(request):

    if request.method == 'POST':

        validators = FormLoginValidator(request.POST)

        if validators.is_valid():

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
     elif User.groups.filter(id=STATIC_ROLS['Profesores']).exists():
         return True
     else:
        return True

@login_required(login_url="/login-estudiante")
def inicio_estudiante(request):
    usuario = Estudiante.objects.get(id=request.user.id)
    return render_to_response('inicio-estudiante.html', { 'usuario': usuario }, context_instance = RequestContext(request))

@login_required(login_url="/login-estudiante")
def perfil_estudiante(request):
    usuario = Estudiante.objects.get(id=request.user.id)
    return render_to_response('perfil-estudiante.html', { 'usuario': usuario }, context_instance = RequestContext(request))

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

@login_required(login_url="/login-estudiante")
def unidad1_lesson2_tm2(request):
    return render_to_response('../templates/modulo1-unidad1-lesson2-tm2.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson2_tm3(request):
    return render_to_response('../templates/modulo1-unidad1-lesson2-tm3.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson2_tm4(request):
    return render_to_response('../templates/modulo1-unidad1-lesson2-tm4.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson3_tm1(request):
    return render_to_response('../templates/modulo1-unidad1-lesson3-tm1.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson3_tm2(request):
    return render_to_response('../templates/modulo1-unidad1-lesson3-tm2.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson3_tm3(request):
    return render_to_response('../templates/modulo1-unidad1-lesson3-tm3.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson3_tm4(request):
    return render_to_response('../templates/modulo1-unidad1-lesson3-tm4.html')  

@login_required(login_url="/login-estudiante")
def unidad1_lesson4_tm1(request):
    return render_to_response('../templates/modulo1-unidad1-lesson4-tm1.html')  

@login_required(login_url="/login-estudiante")
def unidad1_lesson4_tm2(request):
    return render_to_response('../templates/modulo1-unidad1-lesson4-tm2.html')  


@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def inicio_profesor(request):
    usuario = Profesor.objects.get(id=request.user.id)
    return render_to_response('../templates/inicio-profe.html', { 'usuario': usuario }, context_instance = RequestContext(request))

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def primer_modulo(request):
    estudiantes = Estudiante.objects.filter()
    return render_to_response('../templates/primer-modulo.html', {'estudiantes': estudiantes})

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def primer_modulo_estudiantes(request):
    estudiantes = Estudiante.objects.filter()
    return render_to_response('../templates/primer-modulo-estudiantes.html', {'estudiantes': estudiantes},
                                  context_instance=RequestContext(request))

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def primer_modulo_notas(request):
    return render_to_response('../templates/primer-modulo-notas.html')

from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.hashers import make_password
from django.db import transaction
@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
@transaction.atomic
def registro_estudiante(request):

    error = False
    if request.method == 'POST':
        validators = FormRegistroValidator(request.POST)
        validators.required = ['nombre', 'apellidos', 'email', 'documento', 'sexo', 'username', 'password1']

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

            #TODO: ENviar correo electronico para confirmar cuenta
            asunto = "Registro en English Easy"
            body = render_to_string('email.html', {'user': usuario})

            #send_mail(asunto, body, EMAIL_HOST_USER, [ usuario.email ] )
            # msg = EmailMultiAlternatives(asunto, body, EMAIL_HOST_USER, [usuario.email])
            # msg.content_subtype = "html"
            # msg.send()

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
        buscar = request.GET['identificacion']
        qset = (Q(documento__icontains=buscar) )
        estudiante = Estudiante.objects.filter(qset).first()

    return render_to_response('registro-estudiante.html', {'estudiante': estudiante, 'filtro': buscar},
                              context_instance=RequestContext(request))

def buscar_estudiante1(request):

    estudiante = None
    buscar = None
    if 'buscar' in request.GET.keys():
        buscar = request.GET['identificacion']
        qset = (Q(documento__icontains=buscar) )
        estudiante = Estudiante.objects.filter(qset).first()

    return render_to_response('eliminar-estudiante.html', {'estudiante': estudiante, 'filtro': buscar},
                              context_instance=RequestContext(request))

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def perfil_profesor(request):
    usuario = Profesor.objects.get(id=request.user.id)
    return render_to_response('../templates/perfil-profe.html', { 'usuario': usuario }, context_instance = RequestContext(request))

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

    return render_to_response('../templates/perfil-profe.html',{ "usuario": usu } ,  context_instance = RequestContext(request))

def modificar_perfil_est(request):

    error = False
    if request.method == 'POST':
        usu = User.objects.get( id = request.user.id )
        usu.email = request.POST['email']
        usu.save()

        miusuario = Estudiante()
        miusuario.id = usu
        miusuario.documento = request.POST['documento']
        miusuario.tel = request.POST['tel']
        miusuario.direccion = request.POST['direccion']
        miusuario.fecha_nacimiento = request.POST['nacimiento']
        miusuario.save()

        if request.user.groups.filter(id=STATIC_ROLS['Estudiantes']).exists():
            usuario_int = Estudiante.objects.get(id__id=request.user.id)
        else:
            usuario_int = None

    return render_to_response('../templates/perfil-estudiante.html',{ "usuario":  miusuario } ,  context_instance = RequestContext(request))

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def modificar_contra_profesor(request):

    error = False
    usu1 = None
    if request.method == 'POST':
        usu1 = User.objects.get(id=request.user.id)
        usu1.password = make_password(request.POST['password1'])
        usu1.save()

    return render_to_response('../templates/modificar_contraseña.html', { 'usuario': usu1 }, context_instance = RequestContext(request))

@login_required(login_url="/login-estudiante")
def modificar_contra_estudiante(request):

    error = False
    usu1 = None
    if request.method == 'POST':
        usu1 = User.objects.get(id=request.user.id)
        usu1.password = make_password(request.POST['password1'])
        usu1.save()

    return render_to_response('../templates/modificar-contra-est.html', { 'usuario': usu1 }, context_instance = RequestContext(request))

@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def eliminar_estudiante(request):

    return render_to_response('../templates/eliminar-estudiante.html', context_instance=RequestContext(request))

import simplejson
@login_required(login_url="/login-profesor")
@user_passes_test(restringir_estudiante, login_url='/login-profesor')
def elimina_est(request, pk):

    pks = request.POST.get('pk')
    estudiante = User.objects.get(pk=pks)
    estudiante.delete()
    return HttpResponseRedirect('/eliminar-estudiante')


import xhtml2pdf.pisa as pisa
from StringIO import StringIO
from django.template.loader import render_to_string
from english.settings import STATICFILES_DIRS
def pdf(f):
    def funcion(*args, **kwargs):
        html = f(*args, **kwargs)
        result = StringIO() #creamos una instancia del un objeto StringIO para
        pdf = pisa.pisaDocument( html , result) # convertimos en pdf la template
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return funcion

@pdf
def reporte_estudiante(request):
    estudiantes = Estudiante.objects.filter()
    return render_to_string("reporte_estudiantes.html", { 'estudiantes': estudiantes, 'path': STATICFILES_DIRS[0] }) #obtenemos la plantilla

import xhtml2pdf.pisa as pisa
from StringIO import StringIO
from django.template.loader import render_to_string
#def reporte(request):
#    result = StringIO() #creamos una instancia del un objeto StringIO para
#    html = render_to_string("reporte_estudiantes.html", {"user": 'Docente'}) #obtenemos la plantilla
#    pdf = pisa.pisaDocument( html , result) # convertimos en pdf la template
#    return HttpResponse(result.getvalue(), content_type='application/pdf')