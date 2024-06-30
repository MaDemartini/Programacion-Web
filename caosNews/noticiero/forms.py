from django import forms
from PIL import Image
from .models import Genero, Noticiero, Noticia, Subscription

# Formulario para el modelo Genero
class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['genero']

# Formulario para el modelo Noticiero
class NoticieroForm(forms.ModelForm):
    class Meta:
        model = Noticiero
        fields = ['rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'id_genero', 'telefono', 'email', 'direccion', 'activo']

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'autor', 'fecha_publicacion', 'categoria', 'contenido', 'imagen', 'imagen2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs['accept'] = 'image/*'
        self.fields['imagen2'].widget.attrs['accept'] = 'image/*'

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            # Verificar el tamaño
            if imagen.size > 2 * 1024 * 1024:  # Tamaño máximo de 2MB
                raise forms.ValidationError("La imagen principal no puede superar los 2MB.")

            # Verificar las dimensiones (opcional)
            image = Image.open(imagen)
            width, height = image.size
            if width > 1200 or height > 1200:  # Ejemplo: limitar a 1200x1200
                raise forms.ValidationError("La imagen principal no puede tener más de 1200x1200 píxeles.")

        return imagen

    def clean_imagen2(self):
        imagen2 = self.cleaned_data.get('imagen2')
        if imagen2:
            # Verificar el tamaño
            if imagen2.size > 2 * 1024 * 1024:  # Tamaño máximo de 2MB
                raise forms.ValidationError("La imagen secundaria no puede superar los 2MB.")

            # Verificar las dimensiones (opcional)
            image = Image.open(imagen2)
            width, height = image.size
            if width > 1200 or height > 1200:  # Ejemplo: limitar a 1200x1200
                raise forms.ValidationError("La imagen secundaria no puede tener más de 1200x1200 píxeles.")

        return imagen2
    
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = []