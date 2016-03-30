from django.conf.urls import url
from django.contrib import admin
from project.views import *

urlpatterns = [
    url(r'^$', index, name='index' ), #/
    url(r'^curso$', curso, name='curso' ), #/curso
    url(r'^login-estudiante$', login_estudiante, name='login-estudiante' ), #/login
    url(r'^login-profesor$', login_profesor, name='login-profesor' ), #/login
    url(r'^inicio$', inicio_estudiante, name='inicio-estudiante' ),#/Inicio-estudiante
    url(r'^modulo1$', modulo1, name='modulo1' ), #/modulo1
    url(r'^unidad1$', modulo1_unidad1, name='modulo1-unidad1' ), #/unidad1
    url(r'^tema1$', unidad1_tm1, name='modulo1-unidad1-tm1' ), #/tema1
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^admin/', admin.site.urls),
]
