from django.conf.urls import url, include
from django.contrib import admin
from project.views import *

urlpatterns = [
    url(r'^$', index, name='index' ), #/
    url(r'^institution$', curso, name='curso' ), #/curso
    url(r'^contacto$', contacto, name='contacto'),  # /contacto
    url(r'^contacto-f$', contacto_f, name='contacto-f'),
    url(r'^login-estudiante$', login_estudiante, name='login-estudiante' ), #/login-estudiante
    url('^logout$', logout, name = 'logout' ), #/login
    url(r'^login-profesor$', login_profesor, name='login-profesor' ), #/login-profesor

    url(r'^inicio-estudiante$', inicio_estudiante, name='inicio-estudiante' ),#/Inicio-estudiante
    url(r'^perfil-estudiante$', perfil_estudiante, name='perfil-estudiante'),  # /perfil-estudiante
    url(r'^modificar-contra-estudiante$', modificar_contra_estudiante, name='modificar-contra-estudiante'), # /modificar-contra-est

    url(r'^multimedia$', multimedia, name='multimedia' ), 
    url(r'^modulo1$', modulo1, name='modulo1' ), #/modulo1

    url(r'^unidad1$', modulo1_unidad1, name='modulo1-unidad1' ), #/unidad1
    url(r'^unidad2$', modulo1_unidad2, name='modulo1-unidad2' ), #/unidad2
    url(r'^unidad3$', modulo1_unidad3, name='modulo1-unidad3' ), #/unidad3

# <------------------------- Modulo 1 ----------------------------------------------->

    url(r'^lesson1-tema2$', unidad1_tm1, name='modulo1-unidad1-tm1' ), #/tema2
    url(r'^lesson1-tema1$', unidad1_lesson1_tm2, name='modulo1-unidad1-lesson1-tm2'),  # /lesson1-tema1
    url(r'^lesson1-tema3$', unidad1_lesson1_tm3, name='modulo1-unidad1-lesson1-tm3'),  # /lesson1-tema3
    url(r'^lesson1-tema4$', unidad1_lesson1_tm4, name='modulo1-unidad1-lesson1-tm4'),  # /lesson1-tema4

    url(r'^lesson2-tema1$', unidad1_lesson2_tm1, name='modulo1-unidad1-lesson2-tm1'),  # /lesson2-tema1
    url(r'^lesson2-tema2$', unidad1_lesson2_tm2, name='modulo1-unidad1-lesson2-tm2'),  # /lesson2-tema2
    url(r'^lesson2-tema3$', unidad1_lesson2_tm3, name='modulo1-unidad1-lesson2-tm3'),  # /lesson2-tema3
    url(r'^lesson2-tema4$', unidad1_lesson2_tm4, name='modulo1-unidad1-lesson2-tm4'),  # /lesson2-tema4

    url(r'^lesson3-tema1$', unidad1_lesson3_tm1, name='modulo1-unidad1-lesson3-tm1'),  # /lesson3-tema1
    url(r'^lesson3-tema2$', unidad1_lesson3_tm2, name='modulo1-unidad1-lesson3-tm2'),  # /lesson3-tema2
    url(r'^lesson3-tema3$', unidad1_lesson3_tm3, name='modulo1-unidad1-lesson3-tm3'),  # /lesson3-tema3
    url(r'^lesson3-tema4$', unidad1_lesson3_tm4, name='modulo1-unidad1-lesson3-tm4'),  # /lesson3-tema4

    url(r'^lesson4-tema1$', unidad1_lesson4_tm1, name='modulo1-unidad1-lesson4-tm1'),  # /lesson4-tema1
    url(r'^lesson4-tema2$', unidad1_lesson4_tm2, name='modulo1-unidad1-lesson4-tm2'),  # /lesson4-tema2
    url(r'^lesson4-tema3$', unidad1_lesson4_tm3, name='modulo1-unidad1-lesson4-tm3'),  # /lesson4-tema3
    url(r'^lesson4-tema4$', unidad1_lesson4_tm4, name='modulo1-unidad1-lesson4-tm4'),  # /lesson4-tema3

    url(r'^lesson5-tema1$', unidad1_lesson5_tm1, name='modulo1-unidad1-lesson5-tm1'),  # /lesson5-tema1
    url(r'^lesson5-tema2$', unidad1_lesson5_tm2, name='modulo1-unidad1-lesson5-tm2'),  # /lesson5-tema2
    url(r'^lesson5-tema3$', unidad1_lesson5_tm3, name='modulo1-unidad1-lesson5-tm3'),  # /lesson5-tema3
    url(r'^lesson5-tema4$', unidad1_lesson5_tm4, name='modulo1-unidad1-lesson5-tm4'),  # /lesson5-tema4

    url(r'^lesson6-tema1$', unidad1_lesson6_tm1, name='modulo1-unidad1-lesson6-tm1'),  # /lesson6-tema1
    url(r'^lesson6-tema2$', unidad1_lesson6_tm2, name='modulo1-unidad1-lesson6-tm2'),  # /lesson6-tema2
    url(r'^lesson6-tema3$', unidad1_lesson6_tm3, name='modulo1-unidad1-lesson6-tm3'),  # /lesson6-tema3
    url(r'^lesson6-tema4$', unidad1_lesson6_tm4, name='modulo1-unidad1-lesson6-tm4'),  # /lesson6-tema4

    url(r'^lesson7-tema1$', unidad1_lesson7_tm1, name='modulo1-unidad1-lesson7-tm1'),  # /lesson7-tema1
    url(r'^lesson7-tema2$', unidad1_lesson7_tm2, name='modulo1-unidad1-lesson7-tm2'),  # /lesson7-tema2
    url(r'^lesson7-tema3$', unidad1_lesson7_tm3, name='modulo1-unidad1-lesson7-tm3'),  # /lesson7-tema3
    url(r'^lesson7-tema4$', unidad1_lesson7_tm4, name='modulo1-unidad1-lesson7-tm4'),  # /lesson7-tema4

    url(r'^lesson8-tema1$', unidad1_lesson8_tm1, name='modulo1-unidad1-lesson8-tm1'),  # /lesson8-tema1
    url(r'^lesson8-tema2$', unidad1_lesson8_tm2, name='modulo1-unidad1-lesson8-tm2'),  # /lesson8-tema2
    url(r'^lesson8-tema3$', unidad1_lesson8_tm3, name='modulo1-unidad1-lesson8-tm3'),  # /lesson8-tema3
    url(r'^lesson8-tema4$', unidad1_lesson8_tm4, name='modulo1-unidad1-lesson8-tm4'),  # /lesson8-tema4

# <--------------------------- Modulo 2 -------------------------------------------------->

    url(r'^module2/unity1/lesson1/theme1$', modulo2_unidad1_lesson1_tm1, name='modulo2-unidad1-lesson1-tm1'),  
    

    url(r'^home$', inicio_profesor, name='inicio-profesor' ),#/Inicio-profesor
    url(r'^profile$', perfil_profesor, name='perfil-profesor'),  # /perfil-profesor
    url(r'^primer-modulo$', primer_modulo, name='primer-modulo'),  # /primer-modulo-panel
    url(r'^primer-modulo-notas$', primer_modulo_notas, name='primer-modulo-notas'),  # /primer-modulo-notas-panel

    url(r'^student/add$', registro_estudiante, name='registro-estudiante' ), #/registro-estudiante
    url(r'^student/delete$', eliminar_estudiante, name='eliminar-estudiante'),  # /eliminar-estudiante
    url(r'^eliminar-estudiante/(?P<pk>\d+)/remove$', elimina_est, name='elimina-est'),  # /eliminar-estudiante
    url(r'^modificar-contra-profesor$', modificar_contra_profesor, name='modificar-contra-profesor'),  # /modificar-contra

    url(r'^groups$', lista_grupos, name='lista-grupos'),
    url(r'^groups/add$', createGrupos.as_view(), name='agregar-grupos'),
    url(r'^groups/(?P<pk>[0-9]+)/edit$', editGrupos.as_view(), name='editar-grupos'),
    url(r'^groups/(?P<pk>\d+)/delete/$', deleteGrupos.as_view(), name='eliminar-grupos'),
    url(r'^groups/students/(?P<pk>[0-9]+)$', grupos_estudiantes, name='grupos-estudiantes'),  

    url(r'^curso$', lista_curso, name='lista-curso'),
    url(r'^curso/add$', agregar_curso, name='agregar-curso'),
    url(r'^curso/(?P<pk>[0-9]+)/edit/$', editar_curso, name='editar-curso'),
    url(r'^curso/(?P<pk>\d+)/remove/$', eliminar_curso, name='eliminar-curso'),

    url('^buscar_estudiante$', buscar_estudiante, name='buscar_estudiante'),
    url('^buscar_estudiante1$', buscar_estudiante1, name='buscar_estudiante1'),
    url('^modificar-perfil$', modificar_perfil, name='modificar-perfil'),
    url('^modificar-perfil-est$', modificar_perfil_est, name='modificar-perfil-est'),
    url('^reporte-estudiante$', reporte_estudiante, name='reporte-estudiante'),

    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
]
