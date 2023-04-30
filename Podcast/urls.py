from django.urls import path
from Podcast import views


urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('programas/', views.ListaProgramas.as_view(), name='lista_programas'),
    path('programas/crear/', views.CrearPrograma.as_view(), name='crear_programa'),
    path('programas/<int:pk>', views.MostrarPrograma.as_view(), name='mostrar_programa'),
    path('programas/<int:pk>/modificar', views.ModificarPrograma.as_view(), name='modificar_programa'),
    path('programas/<int:pk>/eliminar', views.EliminarPrograma.as_view(), name='eliminar_programa'),
]