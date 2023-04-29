from django.urls import path
from Podcast import views


urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('cargar-programa/', views.carga_formulario, name='carga_formulario'),
    path('lista-programas/', views.lista_programas, name='lista_programas'),
]