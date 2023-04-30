from django.shortcuts import render, redirect
from Podcast.models import Programa
from Podcast.forms import CreacionProgramaFormulario, BuscarPrograma
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.

#Vista para la pantalla de inicio de la Aplicacion Podcast
def mi_vista(request):
    return render(request,'Podcast/index.html',)

#vista sobre mi
def sobre_mi(request):
    return render(request, 'Podcast/sobre_mi.html')


#Vista destinada a poblar la base de datos.
# def crear_programa(request):
#     if request.method == 'POST':
#         formulario = CreacionProgramaFormulario(request.POST)
#         if formulario.is_valid():
#             datos_correctos = formulario.cleaned_data
#             programa = Programa(nombre= datos_correctos ['nombre'], genero= datos_correctos ['genero'], idioma= datos_correctos ['idioma'], fecha_lanzamiento= datos_correctos ['fecha_lanzamiento'], productora= datos_correctos ['productora'],descripcion= datos_correctos ['descripcion'])
#             programa.save()
#             return redirect('lista_programas')
#     formulario = CreacionProgramaFormulario()
#     return render(request, 'Podcast/crear_programa.html', {'formulario': formulario})


#Vista destinada a poblar la base de datos (por CBV).
class CrearPrograma(CreateView):
	model = Programa
	template_name = 'Podcast/CBV/crear_programa.html'
	success_url = '/Podcast/programas/'
	fields = ['nombre','genero','idioma','fecha_lanzamiento','productora','descripcion']		 
        

#Vista destinada a ver y buscar datos de la base de datos (por vista clasica para poder usar decoradores).
# def lista_programas(request):
#     programa_a_buscar = request.GET.get('nombre', None)
#     if programa_a_buscar:
#         programas = Programa.objects.filter(nombre__icontains=programa_a_buscar)
#     else:
#         programas = Programa.objects.all()
#     formulario_busqueda = BuscarPrograma()
#     return render(request, 'Podcast/lista_programa.html', {'programas': programas, 'formulario': formulario_busqueda})


class ListaProgramas(ListView):
    #primero le tengo que decir el modelo con el que va a trabajar.
    model = Programa
    #Despues el template con el que va a laburar. Ya no le paso el diccionario sino que recibira el un object_list.
    #generado automaticamente por django
    template_name = 'Podcast/CBV/lista_programas.html'

#Funcion para ver un programa especifico
class MostrarPrograma(DetailView):
    model = Programa
    template_name = 'Podcast/CBV/mostrar_programa.html'
    success_url = '/Podcast/programas/'

#a la clase se le tiene que pasar como argumento UpdateView. Para editar es igual que crear
class ModificarPrograma(UpdateView):
    model = Programa
    template_name = 'Podcast/CBV/modificar_programa.html'
    success_url = '/Podcast/programas/'
    fields = ['nombre','genero','idioma','fecha_lanzamiento','productora','descripcion']	

#a la clase se le tiene que pasar como argumento DeleteView 
class EliminarPrograma(DeleteView):
    model = Programa
    template_name = 'Podcast/CBV/eliminar_programa.html'
    success_url = '/Podcast/programas/'