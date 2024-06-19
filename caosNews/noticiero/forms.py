from django import forms
from .models import Genero, Noticiero

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['genero']

class NoticieroForm(forms.ModelForm):
    class Meta:
        model = Noticiero
        fields = ['rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'id_genero', 'telefono', 'email', 'direccion', 'activo']
