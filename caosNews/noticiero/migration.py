from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Obtener los grupos existentes
grupo_investigador = Group.objects.get(name='Investigador')
grupo_creador = Group.objects.get(name='Creador')

# Obtener los permisos necesarios
permisos_investigador = Permission.objects.filter(codename='view_noticia')
permisos_creador = Permission.objects.filter(
    codename__in=['add_noticia', 'change_noticia', 'delete_noticia']
)

# Asignar permisos a los grupos
grupo_investigador.permissions.add(*permisos_investigador)
grupo_creador.permissions.add(*permisos_creador)
