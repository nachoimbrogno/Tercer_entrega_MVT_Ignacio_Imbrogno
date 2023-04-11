from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from Podcast.models import Programa
from Podcast.forms import CreacionProgramaFormulario

# Create your views here.

def mi_vista(request):
    # return HttpResponse ("<h1>Mi primera vista</h1>")
    return render(request,'Podcast/index.html',)

def carga_formulario(request):
    if request.method == 'POST':
        #Creo un formulario del tipo CreacionAimalFormulario con la info que trae el post.
        formulario = CreacionProgramaFormulario(request.POST)
        #Verifico si el formulario es valido con la info que se nos pasa
        if formulario.is_valid():
            #Ahora le digo que los datos los tome desde
            datos_correctos = formulario.cleaned_data
            programa = Programa(nombre= datos_correctos ['nombre'], genero= datos_correctos ['genero'], idioma= datos_correctos ['idioma'], productora= datos_correctos ['productora'])
            programa.save()
            #Ahora para que vaya al formulario le digo que vaya al lista_formulario para eso cargo redirect en donde
            #exporto los paquetes. listar_aniamles es lo que le defini en name desde urls.py:
            return redirect('lista_programas')
    #en caso que no sea post o no sea valido vendrá aca:
    formulario = CreacionProgramaFormulario()
    return render(request, 'Podcast/carga_formulario.html', {'formulario': formulario})

# def lista_programas(request):
#     #el request.GET es como un diccionario y puedo obtenet la informacion que esta en una llave y sino none
#     nombre_a_buscar = request.GET.get('nombre', None)
#     #Ahora sí, nombre a buscar no esta vacio que devuelva todo, pero si mandan otro filtro los que tiene 
#     #nombre a buscar
#     if nombre_a_buscar:
#         #Busco los animales que yo pongo en nombre a buscar con el get. Lo que hace icontains es buscar los 
#         #que contienen lo que yo quiero buscar y no lo exacto
#         programa = Programa.objects.filter(nombre__icontains=nombre_a_buscar)
#     else:
#         programa = Programa.objects.all()
#     formulario_busqueda = BuscarAnimal()
#     return render(request, 'inicio/lista_animales.html', {'animales': animales, 'formulario': formulario_busqueda})
