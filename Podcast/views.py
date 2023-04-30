from django.shortcuts import render, redirect
from Podcast.models import Programa
from Podcast.forms import CreacionProgramaFormulario, BuscarPrograma


# Create your views here.
#Vista para la pantalla de inicio de la Aplicacion Podcast
def mi_vista(request):
    return render(request,'Podcast/index.html',)

#Vista destinada a poblar la base de datos.
def crear_programa(request):
    if request.method == 'POST':
        formulario = CreacionProgramaFormulario(request.POST)
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
            programa = Programa(nombre= datos_correctos ['nombre'], genero= datos_correctos ['genero'], idioma= datos_correctos ['idioma'], fecha_lanzamiento= datos_correctos ['fecha_lanzamiento'], productora= datos_correctos ['productora'],descripcion= datos_correctos ['descripcion'])
            programa.save()
            return redirect('lista_programas')
    formulario = CreacionProgramaFormulario()
    return render(request, 'Podcast/crear_programa.html', {'formulario': formulario})

#Vista destinada a ver y buscar datos de la base de datos.
def lista_programas(request):
    programa_a_buscar = request.GET.get('nombre', None)
    if programa_a_buscar:
        programas = Programa.objects.filter(nombre__icontains=programa_a_buscar)
    else:
        programas = Programa.objects.all()
    formulario_busqueda = BuscarPrograma()
    return render(request, 'Podcast/lista_programa.html', {'programas': programas, 'formulario': formulario_busqueda})

#vista sobre mi
def sobre_mi(request):
    return render(request, 'Podcast/sobre_mi.html')

