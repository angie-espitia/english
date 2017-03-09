from django import forms
from .models import Curso, Grupo, Estado, Actividades, Preguntas, Respuesta, Grupo_Estudiante, Calificacion

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = ['nombre','fecha_inicio', 'fecha_fin']
        labels = {'nombre': 'Grado',
                  'fecha_inicio': 'Fecha de Inicio',
                  'fecha_fin': 'Fecha de Cierre' 
                 }
        widgets = {'nombre': forms.TextInput(attrs={'class':'form-control'}),
                   'fecha_inicio': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'input_formats': '%d/%m/%Y'}),
                   'fecha_fin': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'input_formats': '%d/%m/%Y'}),
                    }

class GrupoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(GrupoForm, self).__init__(*args, **kwargs)
        # import pdb; pdb.set_trace()
        self.fields['Curso'].queryset = Curso.objects.filter( Profesor_id = user.id )

    class Meta:
        model = Grupo
        fields = ['nombre','jornada', 'Curso']
        labels = {'nombre': 'Nombre',
                  'jornada': 'Jornada',
                  'Curso': 'Curso', 
                 }
        widgets = {'nombre': forms.TextInput(attrs={'class':'form-control'}),
                   'jornada': forms.TextInput(attrs={'class':'form-control'}),
                   'Curso': forms.Select(attrs={'class':'form-control'}),
                    }

class EstadoForm(forms.ModelForm):

    class Meta:
        model = Estado
        fields = ['descripcion']
        labels = {'descripcion': 'Detalle' }
        widgets = {'descripcion': forms.TextInput(attrs={'class':'form-control'}) }

class CalificacionForm(forms.ModelForm):

    class Meta:
        model = Calificacion
        fields = ['nota','detalle' ]
        labels = {'nota': 'Nota',
                  'detalle': 'Detalle',
                 }
        widgets = {'nota': forms.TextInput(attrs={'class':'form-control'}),
                   'detalle': forms.TextInput(attrs={'class':'form-control'}),
                    }
