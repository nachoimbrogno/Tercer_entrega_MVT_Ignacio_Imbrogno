from django import forms

#Formulario para cargar la base de datos
class CreacionProgramaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    idioma = forms.CharField(max_length=30)
    fecha_lanzamiento = forms.DateField()
    productora = forms.CharField(max_length=30)
    descripcion = forms.CharField()

#Formulario para utilizar al momento de buscar en la base
class BuscarPrograma(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
