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
from .models import Estudiante, Profesor, Preguntas, Respuesta, Curso, Grupo, Grupo_Estudiante, Log
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from .forms import GrupoForm, CursoForm
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DeleteView, CreateView


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

@login_required(login_url="/login-estudiante")
def logout(request):
    auth.logout(request)
    log(request, "CERRO_SESION")
    return HttpResponseRedirect("/")

@login_required(login_url="/login-estudiante")
def inicio_estudiante(request):
    usuario = Estudiante.objects.get(id=request.user.id)
    return render(request, 'paginaEstudiante/inicio-estudiante.html', { 'usuario': usuario })

@login_required(login_url="/login-estudiante")
def perfil_estudiante(request):
    usuario = Estudiante.objects.get(id=request.user.id)
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
        miusuario.documento = request.POST['documento']
        miusuario.tel = request.POST['tel']
        miusuario.direccion = request.POST['direccion']
        miusuario.fecha_nacimiento = request.POST['nacimiento']
        miusuario.save()

        if request.user.groups.filter(id=STATIC_ROLS['Estudiantes']).exists():
            usuario_int = Estudiante.objects.get(id__id=request.user.id)
        else:
            usuario_int = None

    return render(request, 'paginaEstudiante/perfil-estudiante.html',{ "usuario":  miusuario } )

@login_required(login_url="/login-estudiante")
def modificar_contra_estudiante(request):
    error = False
    usu1 = None
    if request.method == 'POST':
        usu1 = User.objects.get(id=request.user.id)
        usu1.password = make_password(request.POST['password1'])
        usu1.save()

    return render(request, 'paginaEstudiante/modificar-contra-est.html', { 'usuario': usu1 } )

@login_required(login_url="/login-estudiante")
def multimedia(request):
    return render(request, 'contenidos/multimedia.html')


@login_required(login_url="/login-estudiante")
def modulo1(request):
    return render(request, 'contenidos/unidad1/modulo1.html')

@login_required(login_url="/login-estudiante")
def modulo1_unidad1(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1.html')

@login_required(login_url="/login-estudiante")
def modulo1_unidad2(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad2.html')

@login_required(login_url="/login-estudiante")
def modulo1_unidad3(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad3.html')

@login_required(login_url="/login-estudiante")
def unidad1_tm1(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1 -tm1.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson1_tm2(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson1-tm2.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson1_tm3(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson1-tm3.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson1_tm4(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson1-tm4.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson2_tm1(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson2-tm1.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson2_tm2(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson2-tm2.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson2_tm3(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson2-tm3.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson2_tm4(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson2-tm4.html')

@login_required(login_url="/login-estudiante")
def unidad1_lesson3_tm1(request):
    
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson3-tm1.html' ) 

@login_required(login_url="/login-estudiante")
def unidad1_lesson3_tm2(request):
    preguntas = Preguntas.objects.filter(actividad_id=1)
    preguntas2 = Preguntas.objects.filter(actividad_id=2)
    preguntas3 = Preguntas.objects.filter(actividad_id=3)
    respuesta = Respuesta.objects.filter(pregunta__in = preguntas)
    respuesta2 = Respuesta.objects.filter(pregunta__in = preguntas2)
    respuesta3 = Respuesta.objects.filter(pregunta__in = preguntas3)
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson3-tm2.html', { 'respuesta':respuesta, 'respuesta2':respuesta2, 'respuesta3':respuesta3 }) 

@login_required(login_url="/login-estudiante")
def unidad1_lesson3_tm3(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson3-tm3.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson3_tm4(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson3-tm4.html')  

@login_required(login_url="/login-estudiante")
def unidad1_lesson4_tm1(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson4-tm1.html')  

@login_required(login_url="/login-estudiante")
def unidad1_lesson4_tm2(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson4-tm2.html')  

@login_required(login_url="/login-estudiante")
def unidad1_lesson4_tm3(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson4-tm3.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson4_tm4(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson4-tm4.html')   

@login_required(login_url="/login-estudiante")
def unidad1_lesson5_tm1(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson5-tm1.html')    

@login_required(login_url="/login-estudiante")
def unidad1_lesson5_tm2(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson5-tm2.html')    

@login_required(login_url="/login-estudiante")
def unidad1_lesson5_tm3(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson5-tm3.html')   

@login_required(login_url="/login-estudiante")
def unidad1_lesson5_tm4(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson5-tm4.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson6_tm1(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson6-tm1.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson6_tm2(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson6-tm2.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson6_tm3(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson6-tm3.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson6_tm4(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson6-tm4.html')  

@login_required(login_url="/login-estudiante")
def unidad1_lesson7_tm1(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson7-tm1.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson7_tm2(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson7-tm2.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson7_tm3(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson7-tm3.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson7_tm4(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson7-tm4.html')  

@login_required(login_url="/login-estudiante")
def unidad1_lesson8_tm1(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson8-tm1.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson8_tm2(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson8-tm2.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson8_tm3(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson8-tm3.html') 

@login_required(login_url="/login-estudiante")
def unidad1_lesson8_tm4(request):
    return render(request, 'contenidos/unidad1/modulo1-unidad1-lesson8-tm4.html')                  


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
def primer_modulo_notas(request):
    return render(request, 'paginaDocente/primer-modulo-notas.html')

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

    return render(request, 'paginaDocente/modificar_contraseña.html', { 'usuario': usu1 } )

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
    usu = request.user
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.Profesor_id = usu.id
            curso.save()
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
def reporte_estudiante(request):
    estudiantes = Estudiante.objects.filter()
    return render_to_string("reporte_estudiantes.html", { 'estudiantes': estudiantes, 'path': STATICFILES_DIRS[0] }) #obtenemos la plantilla


def log(request, action):
    log = Log()
    log.usuario = request.user.id
    if(Estudiante.objects.get(id=request.user.id)):
        log.tipo = 'E'
    else:
        log.tipo = 'P'
    log.accion = action
    log.save() 
