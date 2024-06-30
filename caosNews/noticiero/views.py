from django.shortcuts import render, redirect, get_object_or_404
from .models import Genero, Noticiero, Noticia, Subscripcion, Subscription
from .forms import GeneroForm, NoticieroForm, NoticiaForm, SubscriptionForm
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .cart import Cart
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login


# Create your views here.

# Noticias/
def noticiaAntarticarealidadvirtual(request):
    context = {}
    return render(request, 'noticiero/noticias/html/noticiaAntarticarealidadvirtual.html', context)

def noticiaChilecaidanegocios(request):
    context = {}
    return render(request, 'noticiero/noticias/html/noticiaChilecaidanegocios.html', context)

def noticiaFiltracion(request):
    context = {}
    return render(request, 'noticiero/noticias/html/noticiaFiltracion.html', context)

def noticiaMonjanunoa(request):
    context = {}
    return render(request, 'noticiero/noticias/html/noticiaMonjanunoa.html', context)

def noticiaronaldpolitico(request):
    context = {}
    return render(request, 'noticiero/noticias/html/noticiaronaldpolitico.html', context)

def noticiaSteam(request):
    context = {}
    return render(request, 'noticiero/noticias/html/noticiaSteam.html', context)

def noticiasYolviGonzalez(request):
    context = {}
    return render(request, 'noticiero/noticias/html/noticiasYolviGonzalez.html', context)


# Vistas
def subscripciones(request):
    context = {}
    return render(request, 'noticiero/Vistas/subscripciones.html', context)

def categoria(request):
    context = {}
    return render(request, 'noticiero/vistas/categoria.html', context)

def contacto(request):
    context = {}
    return render(request, 'noticiero/vistas/contacto.html', context)

def sobreNosotros(request):
    context = {}
    return render(request, 'noticiero/vistas/sobreNosotros.html', context)

def UneNosotros(request):
    if request.method == 'POST':
        form = NoticieroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página 'index' después de guardar correctamente
    else:
        form = NoticieroForm()
    
    context = {'form': form}
    return render(request, 'noticiero/vistas/uneNosotros.html', context)

def carro(request):
    context = {}
    return render(request, 'noticiero/vistas/carro.html', context)

# INDEX PRINCIPAL
def index(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiero/index.html', {'noticias': noticias})



#------------------------------------------------------------------------------------------



# CRUD 
@staff_member_required
def listadoSQL(request):
    noticieros = Noticiero.objects.raw('SELECT * FROM noticiero_noticiero')
    context = {'noticieros': noticieros}
    return render(request, 'noticiero/VistaAdmin/Crud/listadoSQL.html', context)

@staff_member_required
def crud(request):
    users = User.objects.all()
    noticieros = Noticiero.objects.all()
    subscriptions = Subscription.objects.all()
    context = {
        'users': users,
        'noticieros': noticieros,
        'subscriptions': subscriptions
    }
    return render(request, 'noticiero/VistaAdmin/Crud/crud.html',context)

# Vistas CRUD para Genero
@staff_member_required
def genero_list(request):
    generos = Genero.objects.all()
    return render(request, 'noticiero/VistaAdmin/Crud/genero_list.html', {'generos': generos})


def genero_add(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genero_list')
    else:
        form = GeneroForm()
    return render(request, 'noticiero/VistaAdmin/Crud/genero_add.html', {'form': form})

@login_required
def genero_edit(request, id_genero):
    genero = get_object_or_404(Genero, id_genero=id_genero)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect('genero_list')
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'noticiero/VistaAdmin/Crud/genero_edit.html', {'form': form})

@staff_member_required
def genero_delete(request, id_genero):
    genero = get_object_or_404(Genero, id_genero=id_genero)
    if request.method == 'POST':
        genero.delete()
        return redirect('genero_list')
    return render(request, 'noticiero/VistaAdmin/Crud/genero_delete.html', {'genero': genero})

# Vistas CRUD para Noticiero
# Listar todos los noticieros
@staff_member_required
def noticiero_list(request):
    noticieros = Noticiero.objects.all()
    return render(request, 'noticiero/VistaAdmin/Crud/noticiero_list.html', {'noticieros': noticieros})

# Agregar un nuevo noticiero
@staff_member_required
def noticiero_add(request):
    if request.method == 'POST':
        form = NoticieroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noticiero_list')
    else:
        form = NoticieroForm()
    return render(request, 'noticiero/VistaAdmin/Crud/noticiero_add.html', {'form': form})

# Editar un noticiero existente
@staff_member_required
def noticiero_edit(request, rut):
    noticiero = get_object_or_404(Noticiero, rut=rut)
    if request.method == 'POST':
        form = NoticieroForm(request.POST, instance=noticiero)
        if form.is_valid():
            form.save()
            return redirect('noticiero_list')
    else:
        form = NoticieroForm(instance=noticiero)
    return render(request, 'noticiero/VistaAdmin/Crud/noticiero_edit.html', {'form': form})

# Eliminar un noticiero existente
@staff_member_required
def noticiero_delete(request, rut):
    noticiero = get_object_or_404(Noticiero, rut=rut)
    if request.method == 'POST':
        noticiero.delete()
        return redirect('noticiero_list')
    return render(request, 'noticiero/VistaAdmin/Crud/noticiero_delete.html', {'noticiero': noticiero})



#------------------------------------------------------------------------------------------



# Crud Registro 
# Vista de inicio de sesión con intentos y bloqueo temporal
def login_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')  # Cambiado a request.POST.get() para manejar valores nulos
        password = request.POST.get('password')  # Cambiado a request.POST.get() para manejar valores nulos

        # Obtener el contador de intentos y el tiempo de bloqueo de la sesión del usuario
        login_attempts = request.session.get('login_attempts', 0)
        lockout_time = request.session.get('lockout_time')

        if lockout_time and timezone.now() < lockout_time:
            messages.error(request, 'Demasiados intentos fallidos. Por favor, intenta nuevamente en 30 segundos.')
            return redirect('login')  # Ajustado para redirigir correctamente a 'login'

        user = authenticate(request, username=nombre, password=password)  # Corregido 'nombre' a 'username'
        if user is not None:
            login(request, user)
            request.session['login_attempts'] = 0  # Resetear contador de intentos
            request.session.pop('lockout_time', None)  # Eliminar 'lockout_time' de la sesión si existe
            return redirect('index')  # Ajustado para redirigir correctamente a 'index'
        else:
            login_attempts += 1
            request.session['login_attempts'] = login_attempts

            if login_attempts >= 5:
                request.session['lockout_time'] = timezone.now() + timedelta(seconds=30)
                messages.error(request, 'Demasiados intentos fallidos. Por favor, intenta nuevamente en 30 segundos.')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'noticiero/index.html')

# Permiso Creado O staff
def is_creator_or_staff(user):
    return user.is_authenticated and (user.groups.filter(name='Creador').exists() or user.is_staff)

def creator_or_staff_required(view_func):
    decorated_view_func = login_required(user_passes_test(is_creator_or_staff)(view_func))
    return decorated_view_func


# CRUD de noticias
@creator_or_staff_required
def lista_noticias(request):
    if request.user.is_staff:
        noticias = Noticia.objects.all()
    else:
        noticias = Noticia.objects.filter(autor=request.user)
    return render(request, 'noticiero/VistaAdmin/Crud/lista_noticias.html', {'noticias': noticias})

def detalle_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'noticiero/noticias/detalle_noticia.html', {'noticia': noticia})

# Creador o Staff pueden subir noticias
@creator_or_staff_required
@login_required
def subirNoticias(request):
    if not request.user.is_staff and request.user.groups.filter(name='Creador').exists():
        noticias_activas = Noticia.objects.filter(autor=request.user).count()
        if noticias_activas >= 5:
            raise PermissionDenied("No puedes tener más de 5 noticias activas.")

    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user  # Asigna el autor correctamente
            noticia.save()
            return redirect('lista_noticias')
    else:
        form = NoticiaForm()

    context = {
        'form': form,
    }
    return render(request, 'noticiero/vistas/subirNoticias.html', context)

# Creador o Staff pueden crear noticias
@creator_or_staff_required
def crear_noticia(request):
    if not request.user.is_staff and request.user.groups.filter(name='Creador').exists():
        noticias_activas = Noticia.objects.filter(creador=request.user, activa=True).count()
        if noticias_activas >= 5:
            raise PermissionDenied("No puedes tener más de 5 noticias activas.")
    
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar la noticia con el creador actual
            noticia = form.save(commit=False)
            noticia.creador = request.user
            noticia.save()
            return redirect('lista_noticias')
    else:
        form = NoticiaForm()

    return render(request, 'noticiero/noticias/crear_noticia.html', {'form': form})

# Creador o Staff pueden editar noticias
@creator_or_staff_required
def editar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)

    # Verificar permisos: creador puede editar solo sus noticias
    if not request.user.is_staff and not request.user.groups.filter(name='Creador').exists():
        messages.error(request, "No tienes permiso para editar esta noticia.")
        return redirect('lista_noticias')

    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            messages.success(request, "La noticia se ha actualizado correctamente.")
            return redirect('lista_noticias')
    else:
        form = NoticiaForm(instance=noticia)

    return render(request, 'noticiero/noticias/editar_noticia.html', {'form': form, 'noticia': noticia})

# Creador o Staff pueden eliminar noticias
@creator_or_staff_required
def eliminar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)

    # Verificar permisos: creador puede eliminar solo sus noticias
    if not request.user.is_staff and not request.user.groups.filter(name='Creador').exists():
        messages.error(request, "No tienes permiso para eliminar esta noticia.")
        return redirect('lista_noticias')

    if request.method == 'POST':
        noticia.delete()
        messages.success(request, "La noticia se ha eliminado correctamente.")
        return redirect('lista_noticias')

    return render(request, 'noticiero/noticias/eliminar_noticia.html', {'noticia': noticia})

# Cuentas
def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(username=nombre).exists():
            user = User.objects.create_user(username=nombre, email=email, password=password)
            user.save()
            default_group = Group.objects.get(name='Investigador')
            user.groups.add(default_group)
            user.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('index')  # Redirige a la página de inicio o a donde prefieras
        else:
            messages.error(request, 'El nombre de usuario ya está en uso.')
    return render(request, 'noticiero/index.html')


@login_required
def subscribe_as_creator(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.user = request.user
            subscription.is_creator = True
            subscription.is_active = False  # Por defecto, la solicitud no está activa
            subscription.save()
            messages.success(request, 'Solicitud de suscripción enviada. Espere la activación.')
            return redirect('index')  # Redirige a la página principal o donde prefieras
    else:
        form = SubscriptionForm()

    return render(request, 'noticiero/VistaAdmin/subscripciones.html', {'form': form})

from django.contrib.admin.views.decorators import staff_member_required

@login_required
def manage_subscriptions(request):
    subscriptions = Subscription.objects.filter(is_creator=True, is_active=False)

    if request.method == 'POST':
        subscription_id = request.POST.get('subscription_id')
        subscription = Subscription.objects.get(id=subscription_id)
        
        # Activar la suscripción
        subscription.is_active = True
        subscription.save()

        # Obtener el usuario asociado a la suscripción
        user = subscription.user

        # Cambiar el grupo del usuario a "Creador"
        creator_group = Group.objects.get(name='Creador')
        user.groups.clear()  # Limpiar grupos existentes
        user.groups.add(creator_group)  # Agregar grupo "Creador"
        user.save()

        messages.success(request, 'Suscripción activada con éxito. El usuario ahora es un Creador.')
        return redirect('manage_subscriptions')

    return render(request, 'noticiero/VistaAdmin/manage_subscriptions.html', {'subscriptions': subscriptions})

# ADMIN
@staff_member_required
def administracion(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticiero/VistaAdmin/administracion.html', {'noticias': noticias})

# usuarios registrados
@staff_member_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'noticiero/VistaAdmin/Crud/user_list.html', {'users': users})

# usuario registrado
@staff_member_required
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        group_name = request.POST.get('group')
        group = Group.objects.get(name=group_name)

        user.username = username
        user.email = email
        user.groups.clear()
        user.groups.add(group)
        user.save()

        return redirect('user_list')

    groups = Group.objects.all()
    return render(request, 'noticiero/VistaAdmin/Crud/user_edit.html', {'user': user, 'groups': groups})

# usuario registrado
@staff_member_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'noticiero/VistaAdmin/Crud/user_confirm_delete.html', {'user': user})

# usuario actualizacion grupo
def update_user_group(user_id, new_group_name):
    user = User.objects.get(id=user_id)
    new_group = Group.objects.get(name=new_group_name)
    user.groups.clear()  # Clear existing groups
    user.groups.add(new_group)  # Add the new group
    user.save()  # Save the user object

# Listar suscripciones
@staff_member_required
def subscription_list(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'noticiero/VistaAdmin/Crud/subscription_list.html', {'subscriptions': subscriptions})

@staff_member_required
def subscription_edit(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)

    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            messages.success(request, 'Suscripción actualizada correctamente.')
            return redirect('subscription_list')
    else:
        form = SubscriptionForm(instance=subscription)

    return render(request, 'noticiero/VistaAdmin/Crud/subscription_edit.html', {'subscription': subscription, 'form': form})


# Eliminar suscripción
@staff_member_required
def subscription_delete(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        subscription.delete()
        return redirect('subscription_list')
    return render(request, 'noticiero/VistaAdmin/Crud/subscription_confirm_delete.html', {'subscription': subscription})


# Cuenta Usuario
@login_required
def perfil_view(request):
    # Obtener los datos del usuario actual
    user = request.user
    nombre = user.username
    email = user.email
    grupo = user.groups.first() if user.groups.exists() else None

    context = {
        'user': user,  # Pasar el objeto completo de usuario al contexto
        'nombre': nombre,
        'email': email,
        'grupo': grupo,
        'is_creator_or_staff': user.groups.filter(name='Creador').exists() or user.is_staff,
    }

    return render(request, 'noticiero/perfil.html', context)

@login_required
def perfil_editar(request):
    user = request.user

    if request.method == 'POST':
        first_name = request.POST.get('nombre')
        last_name = request.POST.get('apellido')
        email = request.POST.get('email')

        # Validar y actualizar los datos del usuario
        if not first_name:
            messages.error(request, 'El nombre no puede estar vacío.')
        elif not last_name:
            messages.error(request, 'El apellido no puede estar vacío.')
        elif not email:
            messages.error(request, 'El email no puede estar vacío.')
        else:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('perfil')

    return render(request, 'noticiero/VistaAdmin/Crud/perfil_editar.html', {'user': user})


# Carro
@login_required
def carro_view(request):
    cart = Cart(request)
    items = cart.get_cart_items()

    context = {
        'items': items,
    }
    return render(request, 'noticiero/Vistas/carro.html', context)

@login_required
@require_POST
def agregar_al_carrito(request, subscription_id):
    # Busca la suscripción por un identificador único, como el nombre
    subscription = get_object_or_404(Subscripcion, id=subscription_id)
    cart = Cart(request)
    cart.add(subscription)
    return redirect('carro')

@login_required
@require_POST
def eliminar_item(request, item_id):
    cart = Cart(request)
    cart.remove(item_id)

    return JsonResponse({'status': 'Item eliminado del carrito.'})
