from django.contrib import admin
from .models import Genero, Noticiero, Noticia, Subscripcion, Subscription

# Register your models here.

admin.site.register(Genero)
admin.site.register(Noticiero)
admin.site.register(Noticia)
admin.site.register(Subscripcion)
admin.site.register(Subscription)
