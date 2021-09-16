from django.urls import path, re_path
from django.contrib import admin
from project.views import *

urlpatterns = [
    path('', index, name='index' ), #/
    path('institution/', curso, name='curso' ), #/curso
    path('contacto/', contacto, name='contacto'),  # /contacto
    path('contacto-f/', contacto_f, name='contacto-f'),
    path('login-estudiante/', login_estudiante, name='login-estudiante' ), #/login-estudiante
    path('^logout/', logout, name = 'logout' ), #/login
    path('login-profesor/', login_profesor, name='login-profesor' ), #/login-profesor

    path('inicio-estudiante/', inicio_estudiante, name='inicio-estudiante' ),#/Inicio-estudiante
    path('perfil-estudiante/', perfil_estudiante, name='perfil-estudiante'),  # /perfil-estudiante
    path('modificar-contra-estudiante/', modificar_contra_estudiante, name='modificar-contra-estudiante'), # /modificar-contra-est

    path('multimedia/', multimedia, name='multimedia' ),

# <------------------------- Modulo 1 ----------------------------------------------->
    path('modulo1/', modulo1, name='modulo1' ), #/modulo1

    path('unidad1/', modulo1_unidad1, name='modulo1-unidad1' ), #/unidad1
    path('unidad2/', modulo1_unidad2, name='modulo1-unidad2' ), #/unidad2
    path('unidad3/', modulo1_unidad3, name='modulo1-unidad3' ), #/unidad3

    path('lesson1-tema2/', unidad1_tm1, name='modulo1-unidad1-tm1' ), #/tema2
    path('lesson1-tema1/', unidad1_lesson1_tm2, name='modulo1-unidad1-lesson1-tm2'),  # /lesson1-tema1
    path('lesson1-tema3/', unidad1_lesson1_tm3, name='modulo1-unidad1-lesson1-tm3'),  # /lesson1-tema3
    path('lesson1-tema4/', unidad1_lesson1_tm4, name='modulo1-unidad1-lesson1-tm4'),  # /lesson1-tema4

    path('lesson2-tema1/', unidad1_lesson2_tm1, name='modulo1-unidad1-lesson2-tm1'),  # /lesson2-tema1
    path('lesson2-tema2/', unidad1_lesson2_tm2, name='modulo1-unidad1-lesson2-tm2'),  # /lesson2-tema2
    path('lesson2-tema3/', unidad1_lesson2_tm3, name='modulo1-unidad1-lesson2-tm3'),  # /lesson2-tema3
    path('lesson2-tema4/', unidad1_lesson2_tm4, name='modulo1-unidad1-lesson2-tm4'),  # /lesson2-tema4

    path('lesson3-tema1/', unidad1_lesson3_tm1, name='modulo1-unidad1-lesson3-tm1'),  # /lesson3-tema1
    path('lesson3-tema2/', unidad1_lesson3_tm2, name='modulo1-unidad1-lesson3-tm2'),  # /lesson3-tema2
    path('lesson3-tema3/', unidad1_lesson3_tm3, name='modulo1-unidad1-lesson3-tm3'),  # /lesson3-tema3
    path('lesson3-tema4/', unidad1_lesson3_tm4, name='modulo1-unidad1-lesson3-tm4'),  # /lesson3-tema4

    path('lesson4-tema1/', unidad1_lesson4_tm1, name='modulo1-unidad1-lesson4-tm1'),  # /lesson4-tema1
    path('lesson4-tema2/', unidad1_lesson4_tm2, name='modulo1-unidad1-lesson4-tm2'),  # /lesson4-tema2
    path('lesson4-tema3/', unidad1_lesson4_tm3, name='modulo1-unidad1-lesson4-tm3'),  # /lesson4-tema3
    path('lesson4-tema4/', unidad1_lesson4_tm4, name='modulo1-unidad1-lesson4-tm4'),  # /lesson4-tema3

    path('lesson5-tema1/', unidad1_lesson5_tm1, name='modulo1-unidad1-lesson5-tm1'),  # /lesson5-tema1
    path('lesson5-tema2/', unidad1_lesson5_tm2, name='modulo1-unidad1-lesson5-tm2'),  # /lesson5-tema2
    path('lesson5-tema3/', unidad1_lesson5_tm3, name='modulo1-unidad1-lesson5-tm3'),  # /lesson5-tema3
    path('lesson5-tema4/', unidad1_lesson5_tm4, name='modulo1-unidad1-lesson5-tm4'),  # /lesson5-tema4

    path('lesson6-tema1/', unidad1_lesson6_tm1, name='modulo1-unidad1-lesson6-tm1'),  # /lesson6-tema1
    path('lesson6-tema2/', unidad1_lesson6_tm2, name='modulo1-unidad1-lesson6-tm2'),  # /lesson6-tema2
    path('lesson6-tema3/', unidad1_lesson6_tm3, name='modulo1-unidad1-lesson6-tm3'),  # /lesson6-tema3
    path('lesson6-tema4/', unidad1_lesson6_tm4, name='modulo1-unidad1-lesson6-tm4'),  # /lesson6-tema4

    path('lesson7-tema1/', unidad1_lesson7_tm1, name='modulo1-unidad1-lesson7-tm1'),  # /lesson7-tema1
    path('lesson7-tema2/', unidad1_lesson7_tm2, name='modulo1-unidad1-lesson7-tm2'),  # /lesson7-tema2
    path('lesson7-tema3/', unidad1_lesson7_tm3, name='modulo1-unidad1-lesson7-tm3'),  # /lesson7-tema3
    path('lesson7-tema4/', unidad1_lesson7_tm4, name='modulo1-unidad1-lesson7-tm4'),  # /lesson7-tema4

    path('lesson8-tema1/', unidad1_lesson8_tm1, name='modulo1-unidad1-lesson8-tm1'),  # /lesson8-tema1
    path('lesson8-tema2/', unidad1_lesson8_tm2, name='modulo1-unidad1-lesson8-tm2'),  # /lesson8-tema2
    path('lesson8-tema3/', unidad1_lesson8_tm3, name='modulo1-unidad1-lesson8-tm3'),  # /lesson8-tema3
    path('lesson8-tema4/', unidad1_lesson8_tm4, name='modulo1-unidad1-lesson8-tm4'),  # /lesson8-tema4

# <--------------------------- Modulo 2 -------------------------------------------------->
    path('module2/', modulo2, name='modulo2' ), #/modulo1

    path('module2/unity1/', modulo2_unidad1, name='modulo2-unidad1' ), #/unidad1
    path('module2/unity2/', modulo2_unidad2, name='modulo2-unidad2' ), #/unidad2
    path('module2/unity3/', modulo2_unidad3, name='modulo2-unidad3' ), #/unidad3

    path('module2/unity1/lesson1/theme1/', modulo2_unidad1_lesson1_tm1, name='modulo2-unidad1-lesson1-tm1'),
    path('module2/unity1/lesson1/theme2/', modulo2_unidad1_lesson1_tm2, name='modulo2-unidad1-lesson1-tm2'),
    path('module2/unity1/lesson1/theme3/', modulo2_unidad1_lesson1_tm3, name='modulo2-unidad1-lesson1-tm3'),
    path('module2/unity1/lesson1/theme4/', modulo2_unidad1_lesson1_tm4, name='modulo2-unidad1-lesson1-tm4'),

    path('module2/unity1/lesson2/theme1/', modulo2_unidad1_lesson2_tm1, name='modulo2-unidad1-lesson2-tm1'),
    path('module2/unity1/lesson2/theme2/', modulo2_unidad1_lesson2_tm2, name='modulo2-unidad1-lesson2-tm2'),
    path('module2/unity1/lesson2/theme3/', modulo2_unidad1_lesson2_tm3, name='modulo2-unidad1-lesson2-tm3'),
    path('module2/unity1/lesson2/theme4/', modulo2_unidad1_lesson2_tm4, name='modulo2-unidad1-lesson2-tm4'),

    path('module2/unity1/lesson3/theme1/', modulo2_unidad1_lesson3_tm1, name='modulo2-unidad1-lesson3-tm1'),
    path('module2/unity1/lesson3/theme2/', modulo2_unidad1_lesson3_tm2, name='modulo2-unidad1-lesson3-tm2'),
    path('module2/unity1/lesson3/theme3/', modulo2_unidad1_lesson3_tm3, name='modulo2-unidad1-lesson3-tm3'),
    path('module2/unity1/lesson3/theme4/', modulo2_unidad1_lesson3_tm4, name='modulo2-unidad1-lesson3-tm4'),

    path('module2/unity2/lesson4/theme1/', modulo2_unidad2_lesson1_tm1, name='modulo2-unidad2-lesson1-tm1'),
    path('module2/unity2/lesson4/theme2/', modulo2_unidad2_lesson1_tm2, name='modulo2-unidad2-lesson1-tm2'),
    path('module2/unity2/lesson4/theme3/', modulo2_unidad2_lesson1_tm3, name='modulo2-unidad2-lesson1-tm3'),
    path('module2/unity2/lesson4/theme4/', modulo2_unidad2_lesson1_tm4, name='modulo2-unidad2-lesson1-tm4'),

    path('module2/unity2/lesson5/theme1/', modulo2_unidad2_lesson2_tm1, name='modulo2-unidad2-lesson2-tm1'),
    path('module2/unity2/lesson5/theme2/', modulo2_unidad2_lesson2_tm2, name='modulo2-unidad2-lesson2-tm2'),
    path('module2/unity2/lesson5/theme3/', modulo2_unidad2_lesson2_tm3, name='modulo2-unidad2-lesson2-tm3'),
    path('module2/unity2/lesson5/theme4/', modulo2_unidad2_lesson2_tm4, name='modulo2-unidad2-lesson2-tm4'),

    path('module2/unity2/lesson6/theme1/', modulo2_unidad2_lesson3_tm1, name='modulo2-unidad2-lesson3-tm1'),
    path('module2/unity2/lesson6/theme2/', modulo2_unidad2_lesson3_tm2, name='modulo2-unidad2-lesson3-tm2'),
    path('module2/unity2/lesson6/theme3/', modulo2_unidad2_lesson3_tm3, name='modulo2-unidad2-lesson3-tm3'),
    path('module2/unity2/lesson6/theme4/', modulo2_unidad2_lesson3_tm4, name='modulo2-unidad2-lesson3-tm4'),

    path('module2/unity3/lesson7/theme1/', modulo2_unidad3_lesson1_tm1, name='modulo2-unidad3-lesson1-tm1'),
    path('module2/unity3/lesson7/theme2/', modulo2_unidad3_lesson1_tm2, name='modulo2-unidad3-lesson1-tm2'),
    path('module2/unity3/lesson7/theme3/', modulo2_unidad3_lesson1_tm3, name='modulo2-unidad3-lesson1-tm3'),
    path('module2/unity3/lesson7/theme4/', modulo2_unidad3_lesson1_tm4, name='modulo2-unidad3-lesson1-tm4'),

    path('module2/unity3/lesson8/theme1/', modulo2_unidad3_lesson2_tm1, name='modulo2-unidad3-lesson2-tm1'),
    path('module2/unity3/lesson8/theme2/', modulo2_unidad3_lesson2_tm2, name='modulo2-unidad3-lesson2-tm2'),
    path('module2/unity3/lesson8/theme3/', modulo2_unidad3_lesson2_tm3, name='modulo2-unidad3-lesson2-tm3'),
    path('module2/unity3/lesson8/theme4/', modulo2_unidad3_lesson2_tm4, name='modulo2-unidad3-lesson2-tm4'),

 # <--------------------------- Modulo 3 -------------------------------------------------->
    path('module3/', modulo3, name='modulo3' ), #/modulo1

    path('module3/unity1/', modulo3_unidad1, name='modulo3-unidad1' ), #/unidad1
    path('module3/unity2/', modulo3_unidad2, name='modulo3-unidad2' ), #/unidad2
    path('module3/unity3/', modulo3_unidad3, name='modulo3-unidad3' ), #/unidad3

    path('module3/unity1/lesson1/theme1/', modulo3_unidad1_lesson1_tm1, name='modulo3-unidad1-lesson1-tm1'),
    path('module3/unity1/lesson1/theme2/', modulo3_unidad1_lesson1_tm2, name='modulo3-unidad1-lesson1-tm2'),
    path('module3/unity1/lesson1/theme3/', modulo3_unidad1_lesson1_tm3, name='modulo3-unidad1-lesson1-tm3'),
    path('module3/unity1/lesson1/theme4/', modulo3_unidad1_lesson1_tm4, name='modulo3-unidad1-lesson1-tm4'),

    path('module3/unity1/lesson2/theme1/', modulo3_unidad1_lesson2_tm1, name='modulo3-unidad1-lesson2-tm1'),
    path('module3/unity1/lesson2/theme2/', modulo3_unidad1_lesson2_tm2, name='modulo3-unidad1-lesson2-tm2'),
    path('module3/unity1/lesson2/theme3/', modulo3_unidad1_lesson2_tm3, name='modulo3-unidad1-lesson2-tm3'),
    path('module3/unity1/lesson2/theme4/', modulo3_unidad1_lesson2_tm4, name='modulo3-unidad1-lesson2-tm4'),

    path('module3/unity1/lesson3/theme1/', modulo3_unidad1_lesson3_tm1, name='modulo3-unidad1-lesson3-tm1'),
    path('module3/unity1/lesson3/theme2/', modulo3_unidad1_lesson3_tm2, name='modulo3-unidad1-lesson3-tm2'),
    path('module3/unity1/lesson3/theme3/', modulo3_unidad1_lesson3_tm3, name='modulo3-unidad1-lesson3-tm3'),
    path('module3/unity1/lesson3/theme4/', modulo3_unidad1_lesson3_tm4, name='modulo3-unidad1-lesson3-tm4'),

    path('module3/unity2/lesson4/theme1/', modulo3_unidad2_lesson1_tm1, name='modulo3-unidad2-lesson1-tm1'),
    path('module3/unity2/lesson4/theme2/', modulo3_unidad2_lesson1_tm2, name='modulo3-unidad2-lesson1-tm2'),
    path('module3/unity2/lesson4/theme3/', modulo3_unidad2_lesson1_tm3, name='modulo3-unidad2-lesson1-tm3'),
    path('module3/unity2/lesson4/theme4/', modulo3_unidad2_lesson1_tm4, name='modulo3-unidad2-lesson1-tm4'),

    path('module3/unity2/lesson5/theme1/', modulo3_unidad2_lesson2_tm1, name='modulo3-unidad2-lesson2-tm1'),
    path('module3/unity2/lesson5/theme2/', modulo3_unidad2_lesson2_tm2, name='modulo3-unidad2-lesson2-tm2'),
    path('module3/unity2/lesson5/theme3/', modulo3_unidad2_lesson2_tm3, name='modulo3-unidad2-lesson2-tm3'),
    path('module3/unity2/lesson5/theme4/', modulo3_unidad2_lesson2_tm4, name='modulo3-unidad2-lesson2-tm4'),

    path('module3/unity2/lesson6/theme1/', modulo3_unidad2_lesson3_tm1, name='modulo3-unidad2-lesson3-tm1'),
    path('module3/unity2/lesson6/theme2/', modulo3_unidad2_lesson3_tm2, name='modulo3-unidad2-lesson3-tm2'),
    path('module3/unity2/lesson6/theme3/', modulo3_unidad2_lesson3_tm3, name='modulo3-unidad2-lesson3-tm3'),
    path('module3/unity2/lesson6/theme4/', modulo3_unidad2_lesson3_tm4, name='modulo3-unidad2-lesson3-tm4'),

    path('module3/unity3/lesson7/theme1/', modulo3_unidad3_lesson1_tm1, name='modulo3-unidad3-lesson1-tm1'),
    path('module3/unity3/lesson7/theme2/', modulo3_unidad3_lesson1_tm2, name='modulo3-unidad3-lesson1-tm2'),
    path('module3/unity3/lesson7/theme3/', modulo3_unidad3_lesson1_tm3, name='modulo3-unidad3-lesson1-tm3'),
    path('module3/unity3/lesson7/theme4/', modulo3_unidad3_lesson1_tm4, name='modulo3-unidad3-lesson1-tm4'),

    path('module3/unity3/lesson8/theme1/', modulo3_unidad3_lesson2_tm1, name='modulo3-unidad3-lesson2-tm1'),
    path('module3/unity3/lesson8/theme2/', modulo3_unidad3_lesson2_tm2, name='modulo3-unidad3-lesson2-tm2'),
    path('module3/unity3/lesson8/theme3/', modulo3_unidad3_lesson2_tm3, name='modulo3-unidad3-lesson2-tm3'),
    path('module3/unity3/lesson8/theme4/', modulo3_unidad3_lesson2_tm4, name='modulo3-unidad3-lesson2-tm4'),

 # <--------------------------- Modulo 4 -------------------------------------------------->
    path('module4/', modulo4, name='modulo4' ), #/modulo4

    path('module4/unity1/', modulo4_unidad1, name='modulo4-unidad1' ), #/unidad1
    path('module4/unity2/', modulo4_unidad2, name='modulo4-unidad2' ), #/unidad2
    path('module4/unity3/', modulo4_unidad3, name='modulo4-unidad3' ), #/unidad3

    path('module4/unity1/lesson1/theme1/', modulo4_unidad1_lesson1_tm1, name='modulo4-unidad1-lesson1-tm1'),
    path('module4/unity1/lesson1/theme2/', modulo4_unidad1_lesson1_tm2, name='modulo4-unidad1-lesson1-tm2'),
    path('module4/unity1/lesson1/theme3/', modulo4_unidad1_lesson1_tm3, name='modulo4-unidad1-lesson1-tm3'),
    path('module4/unity1/lesson1/theme4/', modulo4_unidad1_lesson1_tm4, name='modulo4-unidad1-lesson1-tm4'),

    path('module4/unity1/lesson2/theme1/', modulo4_unidad1_lesson2_tm1, name='modulo4-unidad1-lesson2-tm1'),
    path('module4/unity1/lesson2/theme2/', modulo4_unidad1_lesson2_tm2, name='modulo4-unidad1-lesson2-tm2'),
    path('module4/unity1/lesson2/theme3/', modulo4_unidad1_lesson2_tm3, name='modulo4-unidad1-lesson2-tm3'),
    path('module4/unity1/lesson2/theme4/', modulo4_unidad1_lesson2_tm4, name='modulo4-unidad1-lesson2-tm4'),

    path('module4/unity1/lesson3/theme1/', modulo4_unidad1_lesson3_tm1, name='modulo4-unidad1-lesson3-tm1'),
    path('module4/unity1/lesson3/theme2/', modulo4_unidad1_lesson3_tm2, name='modulo4-unidad1-lesson3-tm2'),
    path('module4/unity1/lesson3/theme3/', modulo4_unidad1_lesson3_tm3, name='modulo4-unidad1-lesson3-tm3'),
    path('module4/unity1/lesson3/theme4/', modulo4_unidad1_lesson3_tm4, name='modulo4-unidad1-lesson3-tm4'),

    path('module4/unity2/lesson4/theme1/', modulo4_unidad2_lesson1_tm1, name='modulo4-unidad2-lesson1-tm1'),
    path('module4/unity2/lesson4/theme2/', modulo4_unidad2_lesson1_tm2, name='modulo4-unidad2-lesson1-tm2'),
    path('module4/unity2/lesson4/theme3/', modulo4_unidad2_lesson1_tm3, name='modulo4-unidad2-lesson1-tm3'),
    path('module4/unity2/lesson4/theme4/', modulo4_unidad2_lesson1_tm4, name='modulo4-unidad2-lesson1-tm4'),

    path('module4/unity2/lesson5/theme1/', modulo4_unidad2_lesson2_tm1, name='modulo4-unidad2-lesson2-tm1'),
    path('module4/unity2/lesson5/theme2/', modulo4_unidad2_lesson2_tm2, name='modulo4-unidad2-lesson2-tm2'),
    path('module4/unity2/lesson5/theme3/', modulo4_unidad2_lesson2_tm3, name='modulo4-unidad2-lesson2-tm3'),
    path('module4/unity2/lesson5/theme4/', modulo4_unidad2_lesson2_tm4, name='modulo4-unidad2-lesson2-tm4'),

    path('module4/unity2/lesson6/theme1/', modulo4_unidad2_lesson3_tm1, name='modulo4-unidad2-lesson3-tm1'),
    path('module4/unity2/lesson6/theme2/', modulo4_unidad2_lesson3_tm2, name='modulo4-unidad2-lesson3-tm2'),
    path('module4/unity2/lesson6/theme3/', modulo4_unidad2_lesson3_tm3, name='modulo4-unidad2-lesson3-tm3'),
    path('module4/unity2/lesson6/theme4/', modulo4_unidad2_lesson3_tm4, name='modulo4-unidad2-lesson3-tm4'),

    path('module4/unity3/lesson7/theme1/', modulo4_unidad3_lesson1_tm1, name='modulo4-unidad3-lesson1-tm1'),
    path('module4/unity3/lesson7/theme2/', modulo4_unidad3_lesson1_tm2, name='modulo4-unidad3-lesson1-tm2'),
    path('module4/unity3/lesson7/theme3/', modulo4_unidad3_lesson1_tm3, name='modulo4-unidad3-lesson1-tm3'),
    path('module4/unity3/lesson7/theme4/', modulo4_unidad3_lesson1_tm4, name='modulo4-unidad3-lesson1-tm4'),

    path('module4/unity3/lesson8/theme1/', modulo4_unidad3_lesson2_tm1, name='modulo4-unidad3-lesson2-tm1'),
    path('module4/unity3/lesson8/theme2/', modulo4_unidad3_lesson2_tm2, name='modulo4-unidad3-lesson2-tm2'),
    path('module4/unity3/lesson8/theme3/', modulo4_unidad3_lesson2_tm3, name='modulo4-unidad3-lesson2-tm3'),
    path('module4/unity3/lesson8/theme4/', modulo4_unidad3_lesson2_tm4, name='modulo4-unidad3-lesson2-tm4'),


    path('home/', inicio_profesor, name='inicio-profesor' ),#/Inicio-profesor
    path('profile/', perfil_profesor, name='perfil-profesor'),  # /perfil-profesor
    path('primer-modulo/', primer_modulo, name='primer-modulo'),  # /primer-modulo-panel

    path('note/', notas, name='notas'),
    re_path('note/est/(?P<pk>\d+)/', notas_est, name='notas-est'),
    re_path('note/(?P<pk>\d+)/', lista_notas, name='lista-notas'),
    re_path('note/add/(?P<pk>\d+)/student/', agregar_notas, name='agregar-notas'),
    re_path('note/(?P<pk>\d+)/edit/', editar_notas, name='editar-notas'),
    re_path('note/(?P<pk>\d+)/remove/', eliminar_notas, name='eliminar-notas'),
    re_path('note/(?P<pk>\d+)/activity/', guarda_actividad, name='guarda-actividad'),

    path('student/add/', registro_estudiante, name='registro-estudiante' ), #/registro-estudiante
    path('student/delete/', eliminar_estudiante, name='eliminar-estudiante'),  # /eliminar-estudiante
    re_path('eliminar-estudiante/(?P<pk>\d+)/remove/', elimina_est, name='elimina-est'),  # /eliminar-estudiante
    path('modificar-contra-profesor/', modificar_contra_profesor, name='modificar-contra-profesor'),  # /modificar-contra

    path('groups/', lista_grupos, name='lista-grupos'),
    path('groups/add/', createGrupos.as_view(), name='agregar-grupos'),
    re_path('groups/(?P<pk>[0-9]+)/edit/', editGrupos.as_view(), name='editar-grupos'),
    re_path('groups/(?P<pk>\d+)/delete/', deleteGrupos.as_view(), name='eliminar-grupos'),
    re_path('groups/students/(?P<pk>[0-9]+)/', grupos_estudiantes, name='grupos-estudiantes'),
    re_path('groups/students/event/(?P<pk>[0-9]+)/', eventos_estudiantes, name='eventos-estudiantes'),

    path('curso/', lista_curso, name='lista-curso'),
    path('curso/add/', agregar_curso, name='agregar-curso'),
    re_path('curso/(?P<pk>[0-9]+)/edit/', editar_curso, name='editar-curso'),
    re_path('curso/(?P<pk>\d+)/remove/', eliminar_curso, name='eliminar-curso'),

    path('buscar_estudiante/', buscar_estudiante, name='buscar_estudiante'),
    path('buscar_estudiante1/', buscar_estudiante1, name='buscar_estudiante1'),
    path('modificar-perfil/', modificar_perfil, name='modificar-perfil'),
    path('modificar-perfil-est/', modificar_perfil_est, name='modificar-perfil-est'),
    re_path('reporte-estudiante/(?P<pk>[0-9]+)/', reporte_estudiante, name='reporte-estudiante'),

    # path('tinymce/', include('tinymce.paths')),
    path('admin/', admin.site.urls),
]
