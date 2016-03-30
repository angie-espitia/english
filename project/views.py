from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User


def index(request):
    return render_to_response('../templates/index.html')

def curso(request):
    return render_to_response('../templates/curso.html')

def login_estudiante(request):

    user = request.POST.get('username')
    clave = request.POST.get('password')
    correcto = False

    if User.objects.filter(username = user, password = clave).exists():
        correcto = True

    return render_to_response('../templates/login-estudiante.html', ("correcto" , correcto), context_instance= RequestContext(request))

def login_profesor(request):
    return render_to_response('../templates/login-profe.html')

def inicio_estudiante(request):
    return render_to_response('../templates/inicio-estudiante.html')

def modulo1(request):
    return render_to_response('../templates/modulo1.html')

def modulo1_unidad1(request):
    return render_to_response('../templates/modulo1-unidad1.html')

def unidad1_tm1(request):
    return render_to_response('../templates/modulo1-unidad1 -tm1.html')