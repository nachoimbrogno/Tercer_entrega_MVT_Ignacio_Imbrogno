from django import forms

class CreacionProgramaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    idioma = forms.CharField(max_length=30)
    productora = forms.CharField(max_length=30)

# class BuscarAnimal(forms.Form):
#     #Solo buscara por nombre , el required = False me permite que no complete nada en el campo al moento de buscar.
#     nombre = forms.CharField(max_length=20, required=False)