# Tercer_entrega_MVT_Ignacio_Imbrogno
Tercer entrega Ignacio Imbrogno

La entrega esta destinada a armar un blog sobre Podcast. 

En esta en particular la pagina de inicio,que corresponde a la aplicacion "Podcast", se debe probar de la siguiente manera:

http://127.0.0.1:8000/Podcast/

Esa sera la pagina inicial.De ahi hay dos link:

1 - Cargar Programa: Destinado a cargar en la base de datos un progrmaa nuevo. Los datos que pedirá son:
    -Nombre (maximo 50 caracteres).
    -Genero (maximo 50 caracteres).
    -Idioma (maximo 50 caracteres).
    -Productora (maximo 50 caracteres).
Una vez cargado el progrma los llevará a la vista de "Ver Programa" desde la pagina o "lista_programa" desde views 

2 - Ver Programa: Destinado a consultar los programas cargados mediante formulario de Django. La consulta se hace por nombre de podcast (tengo la intencion en el futuro de hacerlo extensivo al resto de los campos)

El programa tambien cuenta con la vista mi_vista que es la inicial de la aplicacion PODCAST.

En cuanto a los templates, el html padre es el padre.html que es el base para todos los otro templates.
Luego los templates index.html(el inicio de la aplicacion PODCAST), lista_programa.html(destinado a mostrar y buscar los podcast cargados en la base) y carga_formulario.html (destinado a cargar la base de datos), TODO ESTOS HEREDAN LAS CONFIGURACION DE padre.html.

Tambien se creó el usuario administrador Admin (sí, con la A) y la password es admin. 
Luego se importó el modelos para poder manejarlo desde el portal de administrador.
Por ultimo se generó el metodo __str__ para darle formato al modelo que se muestra. 