from django.shortcuts import render, redirect, get_object_or_404
from .models import Genero, Noticiero
from .forms import GeneroForm, NoticieroForm    
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

# Noticias/
def noticiaAntarticarealidadvirtual(request):
    context = {}
    return render(request, 'noticiero/noticias/noticiaAntarticarealidadvirtual.html', context)

def noticiaChilecaidanegocios(request):
    context = {}
    return render(request, 'noticiero/noticias/noticiaChilecaidanegocios.html', context)

def noticiaFiltracion(request):
    context = {}
    return render(request, 'noticiero/noticias/noticiaFiltracion.html', context)

def noticiaMonjanunoa(request):
    context = {}
    return render(request, 'noticiero/noticias/noticiaMonjanunoa.html', context)

def noticiaronaldpolitico(request):
    context = {}
    return render(request, 'noticiero/noticias/noticiaronaldpolitico.html', context)

def noticiaSteam(request):
    context = {}
    return render(request, 'noticiero/noticias/noticiaSteam.html', context)

def noticiasYolviGonzalez(request):
    context = {}
    return render(request, 'noticiero/noticias/noticiasYolviGonzalez.html', context)


# Vistas
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

@login_required
def carro(request):
    context = {}
    return render(request, 'noticiero/vistas/carro.html', context)

# INDEX PRINCIPAL
def index(request):
    context = {}
    return render(request, 'noticiero/index.html', context)

def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(username=nombre).exists():
            user = User.objects.create_user(username=nombre, email=email, password=password)
            user.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('index')  # Redirige a la página de inicio o a donde prefieras
        else:
            messages.error(request, 'El nombre de usuario ya está en uso.')
    return render(request, 'noticiero/vistas/registro.html')

# crud sql orm
def listadoSQL(request):
    noticieros = Noticiero.objects.raw('SELECT * FROM noticiero_noticiero')
    context = {'noticieros': noticieros}
    return render(request, 'noticiero/listadoSQL.html', context)

def crud(request):
    noticiero = Noticiero.objects.all()
    context = {'noticiero': noticiero}
    return render(request, 'noticiero/crud.html',context)

# Vistas CRUD para Genero
def genero_list(request):
    generos = Genero.objects.all()
    return render(request, 'noticiero/genero_list.html', {'generos': generos})

def genero_add(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genero_list')
    else:
        form = GeneroForm()
    return render(request, 'noticiero/genero_add.html', {'form': form})

def genero_edit(request, id_genero):
    genero = get_object_or_404(Genero, id_genero=id_genero)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect('genero_list')
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'noticiero/genero_edit.html', {'form': form})

def genero_delete(request, id_genero):
    genero = get_object_or_404(Genero, id_genero=id_genero)
    if request.method == 'POST':
        genero.delete()
        return redirect('genero_list')
    return render(request, 'noticiero/genero_delete.html', {'genero': genero})

# Vistas CRUD para Noticiero

def noticiero_list(request):
    noticieros = Noticiero.objects.all()
    return render(request, 'noticiero/noticiero_list.html', {'noticieros': noticieros})

def noticiero_add(request):
    if request.method == 'POST':
        form = NoticieroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noticiero_list')
    else:
        form = NoticieroForm()
    return render(request, 'noticiero/noticiero_add.html', {'form': form})

def noticiero_edit(request, rut):
    noticiero = get_object_or_404(Noticiero, rut=rut)
    if request.method == 'POST':
        form = NoticieroForm(request.POST, instance=noticiero)
        if form.is_valid():
            form.save()
            return redirect('noticiero_list')
    else:
        form = NoticieroForm(instance=noticiero)
    return render(request, 'noticiero/noticiero_edit.html', {'form': form})

def noticiero_delete(request, rut):
    noticiero = get_object_or_404(Noticiero, rut=rut)
    if request.method == 'POST':
        noticiero.delete()
        return redirect('noticiero_list')
    return render(request, 'noticiero/noticiero_delete.html', {'noticiero': noticiero})




def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(username=nombre).exists():
            user = User.objects.create_user(username=nombre, email=email, password=password)
            user.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('index')  # Redirige a la página de inicio o a donde prefieras
        else:
            messages.error(request, 'El nombre de usuario ya está en uso.')
    return render(request, 'noticiero/vistas/registro.html')

# Vista de inicio de sesión con intentos y bloqueo temporal
def login_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        password = request.POST['password']

        # Obtener el contador de intentos y el tiempo de bloqueo de la sesión del usuario
        login_attempts = request.session.get('login_attempts', 0)
        lockout_time = request.session.get('lockout_time')

        if lockout_time:
            if timezone.now() < lockout_time:
                messages.error(request, 'Demasiados intentos fallidos. Por favor, intenta nuevamente en 30 segundos.')
                return redirect('login')

        user = authenticate(request, nombre=nombre, password=password)
        if user is not None:
            login(request, user)
            request.session['login_attempts'] = 0  # Resetear contador de intentos
            return redirect('index')
        else:
            login_attempts += 1
            request.session['login_attempts'] = login_attempts

            if login_attempts >= 5:
                request.session['lockout_time'] = timezone.now() + timedelta(seconds=30)
                messages.error(request, 'Demasiados intentos fallidos. Por favor, intenta nuevamente en 30 segundos.')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'noticiero/index.html')

