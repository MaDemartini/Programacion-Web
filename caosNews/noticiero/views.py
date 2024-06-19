from django.shortcuts import render, redirect, get_object_or_404
from .models import Genero, Noticiero
from .forms import GeneroForm, NoticieroForm    
# Create your views here.


# Vistas para Genero

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


# Vistas para Noticiero

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
    context = {}
    return render(request, 'noticiero/vistas/UneNosotros.html', context)

def carro(request):
    context = {}
    return render(request, 'noticiero/vistas/carro.html', context)

def registro(request):
    context = {}
    return render(request, 'noticiero/vistas/registro.html', context)


# INDEX PRINCIPAL
def index(request):
    context = {}
    return render(request, 'noticiero/index.html', context)


# crud sql orm
def listadoSQL(request):
    noticiero= Noticiero.objects.raw('SELECT * FROM noticiero_noticiero')
    print(noticiero)
    context = {"noticiero":noticiero}
    return render (request, 'noticiero/listadoSQL.html', context)

def crud(request):
    noticiero = Noticiero.objects.all()
    context = {'noticiero': noticiero}
    return render(request, 'noticiero/crud.html',context)

