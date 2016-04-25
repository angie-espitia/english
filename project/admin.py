from django.contrib import admin
from .models import Profesor, Curso

class CursoChildAdmin(admin.TabularInline):
    model = Curso

@admin.register(Profesor)
class ProfeAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido')
    inlines = [CursoChildAdmin]
    search_fields = ('nombre', 'curso__nombre')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')
