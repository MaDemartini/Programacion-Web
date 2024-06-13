from django.urls import path
from    . import views

urlpatterns = [
    path('categoria', views.categoria, name='categoria'),
    path('contacto', views.contacto, name='contacto'),
    path('', views.index, name='index'),
    path('noticiaAntarticarealidadvirtual', views.noticiaAntarticarealidadvirtual, name='noticiaAntarticarealidadvirtual'),
    path('noticiaChilecaidanegocios', views.noticiaChilecaidanegocios, name='noticiaChilecaidanegocios'),
    path('noticiaFiltracion', views.noticiaFiltracion, name='noticiaFiltracion'),
    path('noticiaMonjanunoa', views.noticiaMonjanunoa, name='noticiaMonjanunoa'),
    path('noticiaronaldpolitico', views.noticiaronaldpolitico, name='noticiaronaldpolitico'),
    path('noticiaSteam', views.noticiaSteam, name='noticiaSteam'),
    path('noticiasYolviGonzalez', views.noticiasYolviGonzalez, name='noticiasYolviGonzalez'),
    path('sobreNosotros', views.sobreNosotros, name='sobreNosotros'),
    path('UneNosotros', views.UneNosotros, name='UneNosotros'),
    path('carro',views.carro, name='carro'),
]
