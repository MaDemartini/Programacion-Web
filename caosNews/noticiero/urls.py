from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    # Páginas principales
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('subscribe_as_creator/', views.subscribe_as_creator, name='subscribe_as_creator'),
    path('manage_subscriptions/', views.manage_subscriptions, name='manage_subscriptions'),

    # Carro de Compras
    path('agregar_al_carrito/<int:subscription_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_item/<int:item_id>/', views.eliminar_item, name='eliminar_item'),

    # Vistas
    path('subscripciones/', views.subscripciones, name='subscripciones'),
    path('categoria/', views.categoria, name='categoria'),
    path('contacto/', views.contacto, name='contacto'),
    path('sobreNosotros/', views.sobreNosotros, name='sobreNosotros'),
    path('UneNosotros/', views.UneNosotros, name='UneNosotros'),
    path('carro/', views.carro, name='carro'),
    path('subirNoticias/', views.subirNoticias, name='subirNoticias'),

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

    # URLs para Noticiero
    path('noticiero_list/', views.noticiero_list, name='noticiero_list'),
    path('noticiero_add/', views.noticiero_add, name='noticiero_add'),
    path('noticiero/edit/<str:rut>/', views.noticiero_edit, name='noticiero_edit'),
    path('noticiero/delete/<str:rut>/', views.noticiero_delete, name='noticiero_delete'),

    # URLs para Género
    path('genero/', views.genero_list, name='genero_list'),
    path('genero/add/', views.genero_add, name='genero_add'),
    path('genero/edit/<int:id_genero>/', views.genero_edit, name='genero_edit'),
    path('genero/delete/<int:id_genero>/', views.genero_delete, name='genero_delete'),

    # URLs para Noticias
    path('noticias/', views.lista_noticias, name='lista_noticias'),
    path('noticias/crear/', views.crear_noticia, name='crear_noticia'),
    path('noticias/<int:pk>/', views.detalle_noticia, name='detalle_noticia'),
    path('noticias/<int:pk>/editar/', views.editar_noticia, name='editar_noticia'),
    path('noticias/<int:pk>/eliminar/', views.eliminar_noticia, name='eliminar_noticia'),

    # Admin 
    path('administracion/', views.administracion, name='administracion'),
    path('users/', views.user_list, name='user_list'),
    path('user/edit/<int:pk>/', views.user_edit, name='user_edit'),
    path('user/delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('subscriptions/', views.subscription_list, name='subscription_list'),
    path('subscription/edit/<int:pk>/', views.subscription_edit, name='subscription_edit'),
    path('subscription/delete/<int:pk>/', views.subscription_delete, name='subscription_delete'),
    
    # URL para ver el perfil del usuario
    path('perfil/', views.perfil_view, name='perfil'),
    path('perfil/editar/', views.perfil_editar, name='perfil_editar'),
    
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)