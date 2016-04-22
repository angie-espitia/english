from django.conf.urls import url, include
from django.contrib import admin
from project.views import *

urlpatterns = [
    url(r'^$', index, name='index' ), #/
    url(r'^curso$', curso, name='curso' ), #/curso
    url(r'^login-estudiante$', login_estudiante, name='login-estudiante' ), #/login-estudiante
    url('^logout$', logout, name = 'logout' ), #/login
    url(r'^login-profesor$', login_profesor, name='login-profesor' ), #/login-profesor
    url('^search$', search, name='search'),

    url(r'^inicio-estudiante$', inicio_estudiante, name='inicio-estudiante' ),#/Inicio-estudiante
    url(r'^modulo1$', modulo1, name='modulo1' ), #/modulo1

    url(r'^unidad1$', modulo1_unidad1, name='modulo1-unidad1' ), #/unidad1
    url(r'^tema1$', unidad1_tm1, name='modulo1-unidad1-tm1' ), #/tema2
    url(r'^tema2$', unidad1_lesson1_tm2, name='modulo1-unidad1-lesson1-tm2'),  # /lesson1-tema1
    url(r'^tema3$', unidad1_lesson1_tm3, name='modulo1-unidad1-lesson1-tm3'),  # /lesson1-tema3
    url(r'^tema4$', unidad1_lesson1_tm4, name='modulo1-unidad1-lesson1-tm4'),  # /lesson1-tema4
    url(r'^tema5$', unidad1_lesson2_tm1, name='modulo1-unidad1-lesson2-tm1'),  # /lesson1-tema4

    url(r'^inicio-profesor$', inicio_profesor, name='inicio-profesor' ),#/Inicio-profesor
    url(r'^primer-modulo$', primer_modulo, name='primer-modulo'),  # /primer-modulo-panel
    url(r'^registro-estudiante$', registro_estudiante, name='registro-estudiante' ), #/registro-estudiante
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^admin/', admin.site.urls),
]
