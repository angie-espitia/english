from django.conf.urls import url, include
from django.contrib import admin
from project.views import *

urlpatterns = [
    url(r'^$', index, name='index' ), #/
    url(r'^curso$', curso, name='curso' ), #/curso
    url(r'^contacto$', contacto, name='contacto'),  # /contacto
    url(r'^contacto-f$', contacto_f, name='contacto-f'),
    url(r'^login-estudiante$', login_estudiante, name='login-estudiante' ), #/login-estudiante
    url('^logout$', logout, name = 'logout' ), #/login
    url(r'^login-profesor$', login_profesor, name='login-profesor' ), #/login-profesor

    url(r'^inicio-estudiante$', inicio_estudiante, name='inicio-estudiante' ),#/Inicio-estudiante
    url(r'^perfil-estudiante$', perfil_estudiante, name='perfil-estudiante'),  # /perfil-estudiante
    url(r'^modificar-contra-estudiante$', modificar_contra_estudiante, name='modificar-contra-estudiante'), # /modificar-contra-est
    url(r'^modulo1$', modulo1, name='modulo1' ), #/modulo1

    url(r'^unidad1$', modulo1_unidad1, name='modulo1-unidad1' ), #/unidad1
    url(r'^tema1$', unidad1_tm1, name='modulo1-unidad1-tm1' ), #/tema2
    url(r'^tema2$', unidad1_lesson1_tm2, name='modulo1-unidad1-lesson1-tm2'),  # /lesson1-tema1
    url(r'^tema3$', unidad1_lesson1_tm3, name='modulo1-unidad1-lesson1-tm3'),  # /lesson1-tema3
    url(r'^tema4$', unidad1_lesson1_tm4, name='modulo1-unidad1-lesson1-tm4'),  # /lesson1-tema4

    url(r'^tema5$', unidad1_lesson2_tm1, name='modulo1-unidad1-lesson2-tm1'),  # /lesson2-tema1
    url(r'^tema6$', unidad1_lesson2_tm2, name='modulo1-unidad1-lesson2-tm2'),  # /lesson2-tema2
    url(r'^tema7$', unidad1_lesson2_tm3, name='modulo1-unidad1-lesson2-tm3'),  # /lesson2-tema3
    url(r'^tema8$', unidad1_lesson2_tm4, name='modulo1-unidad1-lesson2-tm4'),  # /lesson2-tema4

    url(r'^tema9$', unidad1_lesson3_tm1, name='modulo1-unidad1-lesson3-tm1'),  # /lesson3-tema1
    url(r'^tema10$', unidad1_lesson3_tm2, name='modulo1-unidad1-lesson3-tm2'),  # /lesson3-tema2
    url(r'^tema11$', unidad1_lesson3_tm3, name='modulo1-unidad1-lesson3-tm3'),  # /lesson3-tema3
    url(r'^tema12$', unidad1_lesson3_tm4, name='modulo1-unidad1-lesson3-tm4'),  # /lesson3-tema4

    url(r'^tema13$', unidad1_lesson4_tm1, name='modulo1-unidad1-lesson4-tm1'),  # /lesson3-tema1
    url(r'^tema14$', unidad1_lesson4_tm2, name='modulo1-unidad1-lesson4-tm2'),  # /lesson3-tema2

    url(r'^inicio-profesor$', inicio_profesor, name='inicio-profesor' ),#/Inicio-profesor
    url(r'^perfil-profesor$', perfil_profesor, name='perfil-profesor'),  # /perfil-profesor
    url(r'^primer-modulo$', primer_modulo, name='primer-modulo'),  # /primer-modulo-panel
    url(r'^primer-modulo-estudiantes$', primer_modulo_estudiantes, name='primer-modulo-estudiantes'),  # /primer-modulo-estudiantes-panel
    url(r'^primer-modulo-notas$', primer_modulo_notas, name='primer-modulo-notas'),  # /primer-modulo-notas-panel
    url(r'^registro-estudiante$', registro_estudiante, name='registro-estudiante' ), #/registro-estudiante
    url(r'^eliminar-estudiante$', eliminar_estudiante, name='eliminar-estudiante'),  # /eliminar-estudiante
    url(r'^eliminar-estudiante/(?P<pk>\d+)/remove$', elimina_est, name='elimina-est'),  # /eliminar-estudiante
    url(r'^modificar-contra-profesor$', modificar_contra_profesor, name='modificar-contra-profesor'),  # /modificar-contra

    url('^buscar_estudiante$', buscar_estudiante, name='buscar_estudiante'),
    url('^buscar_estudiante1$', buscar_estudiante1, name='buscar_estudiante1'),
    url('^modificar-perfil$', modificar_perfil, name='modificar-perfil'),
    url('^modificar-perfil-est$', modificar_perfil_est, name='modificar-perfil-est'),
    url('^reporte-estudiante$', reporte_estudiante, name='reporte-estudiante'),

    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
]
