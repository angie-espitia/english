from django import forms
from .models import Estudiante
from django.contrib.auth import authenticate
from django.forms import ModelForm


class RegistrarForm(ModelForm):
    password2= forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}),required=False)
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'cedula', 'username', 'password', 'password2' ]

    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2
