from django.shortcuts import render

# Create your views here.


def index(request):
    context={}
    return render(request, 'noticiero/index.html', context)

def categoria(request):
    context={}
    return render(request, 'noticiero/categoria.html', context)

def UneNosotros(request):
    context={}
    return render(request, 'noticiero/UneNosotros.html', context)


