from django.urls import path
from    . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.index, name='contacto'),
    path('UneNosotros', views.index, name='UneNosotros'),
]
