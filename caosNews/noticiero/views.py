from django.shortcuts import render

from .models import Noticiero,Genero
# Create your views here.

def categoria(request):
    context = {}
    return render(request, 'noticiero/categoria.html')

def contacto(request):
    
    context = {}
    return render(request, 'noticiero/contacto.html')

def index(request):
    context = {}
    return render(request, 'noticiero/index.html')

def noticiaAntarticarealidadvirtual(request):
    context = {}
    return render(request, 'noticiero/noticiaAntarticarealidadvirtual.html')

def noticiaChilecaidanegocios(request):
    context = {}
    return render(request, 'noticiero/noticiaChilecaidanegocios.html')

def noticiaFiltracion(request):
    context = {}
    return render(request, 'noticiero/noticiaFiltracion.html')

def noticiaMonjanunoa(request):
    context = {}
    return render(request, 'noticiero/noticiaMonjanunoa.html')

def noticiaronaldpolitico(request):
    context = {}
    return render(request, 'noticiero/noticiaronaldpolitico.html')

def noticiaSteam(request):
    context = {}
    return render(request, 'noticiero/noticiaSteam.html')

def noticiasYolviGonzalez(request):
    context = {}
    return render(request, 'noticiero/noticiasYolviGonzalez.html')

def sobreNosotros(request):
    context = {}
    return render(request, 'noticiero/sobreNosotros.html')

def UneNosotros(request):
    context = {}
    return render(request, 'noticiero/UneNosotros.html')

def carro(request):
    context = {}
    return render(request, 'noticiero/carro.html')


