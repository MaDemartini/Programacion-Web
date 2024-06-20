from django.urls import path
from . import views

urlpatterns = [
    # Páginas principales
    path('', views.index, name='index'),
    path('categoria/', views.categoria, name='categoria'),
    path('contacto/', views.contacto, name='contacto'),
    path('sobreNosotros/', views.sobreNosotros, name='sobreNosotros'),
    path('UneNosotros/', views.UneNosotros, name='UneNosotros'),
    path('carro/', views.carro, name='carro'),

    # Noticias específicas
    path('noticiaAntarticarealidadvirtual/', views.noticiaAntarticarealidadvirtual, name='noticiaAntarticarealidadvirtual'),
    path('noticiaChilecaidanegocios/', views.noticiaChilecaidanegocios, name='noticiaChilecaidanegocios'),
    path('noticiaFiltracion/', views.noticiaFiltracion, name='noticiaFiltracion'),
    path('noticiaMonjanunoa/', views.noticiaMonjanunoa, name='noticiaMonjanunoa'),
    path('noticiaronaldpolitico/', views.noticiaronaldpolitico, name='noticiaronaldpolitico'),
    path('noticiaSteam/', views.noticiaSteam, name='noticiaSteam'),
    path('noticiasYolviGonzalez/', views.noticiasYolviGonzalez, name='noticiasYolviGonzalez'),

    # Operaciones CRUD
    path('listadoSQL/', views.listadoSQL, name='listadoSQL'),
    path('crud/', views.crud, name='crud'),
    path('noticiero_list/', views.noticiero_list, name='noticiero_list'),
    path('noticiero_add/', views.noticiero_add, name='noticiero_add'),
    path('noticiero/edit/<str:rut>/', views.noticiero_edit, name='noticiero_edit'),
    path('noticiero/delete/<str:rut>/', views.noticiero_delete, name='noticiero_delete'),

    # URLs para Género
    path('genero/', views.genero_list, name='genero_list'),
    path('genero/add/', views.genero_add, name='genero_add'),
    path('genero/edit/<int:id_genero>/', views.genero_edit, name='genero_edit'),
    path('genero/delete/<int:id_genero>/', views.genero_delete, name='genero_delete'),
]
