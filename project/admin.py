from django.contrib import admin
from .models import Profesor

#class CursoChildAdmin(admin.TabularInline):
#    model = Curso

@admin.register(Profesor)
class ProfeAdmin(admin.ModelAdmin):
    list_display = ('cedula','profesion')
#    inlines = [CursoChildAdmin]
#    search_fields = ('nombre', 'curso_nombre')

#@admin.register(Curso)
#class CursoAdmin(admin.ModelAdmin):
#    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')
