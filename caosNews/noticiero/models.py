from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modelo para el género
class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return self.genero

# Modelo para la información del noticiero 
class Noticiero(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20) 
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"
    
    class Meta:
        ordering = ['rut']

# Modelo para la información de Noticias
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)  # Cambiar a campo de texto
    fecha_publicacion = models.DateField()
    categoria = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='noticias_imagenes/', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='noticias_imagenes/', blank=True, null=True)

    def __str__(self):
        return self.titulo


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_creator = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)  # Nuevo campo para manejar la activación
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.user.username} - {'Creador' if self.is_creator else 'Investigador'}"


# Modelo para subcripciones
class Subscripcion(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.CharField(max_length=50)
    funciones = models.TextField()
    caracteristicas = models.TextField()
    compatibilidad = models.TextField()
    soporte = models.TextField()

    def __str__(self):
        return self.titulo
    
