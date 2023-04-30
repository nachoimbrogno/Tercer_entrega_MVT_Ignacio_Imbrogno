from django.shortcuts import render, redirect
from Podcast.models import Programa
from Podcast.forms import CreacionProgramaFormulario, BuscarPrograma
#Modulos para poder usar CBV
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
#para usar el lazy en CBV
from django.urls import reverse_lazy
#Importo para poder usar Mixims
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

#Vista para la pantalla de inicio de la Aplicacion Podcast
def mi_vista(request):
    return render(request,'Podcast/index.html',)

#vista sobre mi
def sobre_mi(request):
    return render(request, 'Podcast/sobre_mi.html')

        

#Vista destinada a ver y buscar datos de la base de datos (por vista clasica para poder usar decoradores).
# def lista_programas(request):
#     programa_a_buscar = request.GET.get('nombre', None)
#     if programa_a_buscar:
#         programas = Programa.objects.filter(nombre__icontains=programa_a_buscar)
#     else:
#         programas = Programa.objects.all()
#     formulario_busqueda = BuscarPrograma()
#     return render(request, 'Podcast/lista_programa.html', {'programas': programas, 'formulario': formulario_busqueda})

#Clase para Crear Programa con CBV. Le pongo mixims para que autentique si quiere borrar
class CrearPrograma(LoginRequiredMixin, CreateView):
    model = Programa
    template_name = 'Podcast/CBV/crear_programa.html'
    success_url = reverse_lazy('lista_programas')
    fields = ['nombre','genero','idioma','fecha_lanzamiento','productora','descripcion']		 

#Clase para listar Programa con CBV
class ListaProgramas(ListView):
    model = Programa
    template_name = 'Podcast/CBV/lista_programas.html'

#Clase para Mostrar Programa con CBV
class MostrarPrograma(DetailView):
    model = Programa
    template_name = 'Podcast/CBV/mostrar_programa.html'
    success_url = reverse_lazy('lista_programas')

#Clase para Modificar Programa con CBV. Le pongo mixims para que autentique si quiere borrar
class ModificarPrograma(LoginRequiredMixin, UpdateView):
    model = Programa
    template_name = 'Podcast/CBV/modificar_programa.html'
    success_url = reverse_lazy('lista_programas')
    fields = ['nombre','genero','idioma','fecha_lanzamiento','productora','descripcion']	

#Clase para Eliminar Programa con CBV. Le pongo mixims para que autentique si quiere borrar
class EliminarPrograma(LoginRequiredMixin, DeleteView):
    model = Programa
    template_name = 'Podcast/CBV/eliminar_programa.html'
    success_url = reverse_lazy('lista_programas')