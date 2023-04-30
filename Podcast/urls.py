from django.urls import path
from Podcast import views


urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('programas/', views.lista_programas, name='lista_programas'),
    path('programas/crear', views.crear_programa, name='crear_programa'),
]