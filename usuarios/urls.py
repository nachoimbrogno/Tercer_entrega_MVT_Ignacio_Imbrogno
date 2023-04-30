from django.urls import path
from usuarios import views
#importo par apoder usar el template de logpout
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('cambio-contrasenia/', views.CambioContrasenia.as_view(), name='cambio_contrasenia'),
]