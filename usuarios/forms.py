from django import forms
#Importo forularios de Djanog para crear y modificar usuarios.
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

#creo un formulario "MiFormularioDeCreacion" para poder customizar el registo de usuario ("hereda de UserCreationForm)
class MiFormularioDeCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir Contraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}


#creo un formulario "EdicionDatosUsuario" para poder customizar modificacion de usuario (hereda de UserChangeForm ) 
class EdicionDatosUsuario(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label = 'Nombre', max_length =20)
    last_name = forms.CharField(label = 'Apellido', max_length=20)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']