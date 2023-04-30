from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
#Importo mi formulario creado
from usuarios.forms import MiFormularioDeCreacion, EdicionDatosUsuario
#Para usar reverse lazy
from django.urls import reverse_lazy
#Importo para poder usar decoradores
from django.contrib.auth.decorators import login_required
#Importo para poder usar Mixims
from django.contrib.auth.mixins import LoginRequiredMixin
#Importo para poder usar la clase basada en vista para modificar la contraaseña
from django.contrib.auth.views import PasswordChangeView
#Importo el modelo creado
from usuarios.models import InformacionExtra

# Create your views here.

def login(request):
	return render(request, 'usuarios/login.html')


#Vista para la autenticacion de usuarios
def login(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasenia)
            django_login(request, usuario)
            return redirect ('inicio')
        else:
            return render(request, 'usuarios/login.html',{'formulario':formulario})
    formulario = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'formulario':formulario})

#Vista para el registro de usuario
def registro(request):
    if request.method == "POST":
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect ('login')
        else:
            return render(request, 'usuarios/registro.html',{'formulario':formulario})
    formulario = MiFormularioDeCreacion()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

#Vista para la moficicacion de los datos del usuario, con decorador para usar solo logueado
@login_required
def editar_perfil(request):
    informacion_extra, creado = InformacionExtra.objects.get_or_create(user=request.user)
    if request.method == "POST":
        formulario = EdicionDatosUsuario(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            if formulario.is_valid():
                request.user.informacionextra.avatar = formulario.cleaned_data.get('avatar')
                request.user.informacionextra.descripcion = formulario.cleaned_data.get('descripcion')
            request.user.informacionextra.save()
            formulario.save()
            return redirect ('inicio')
        else:
            return render(request, 'usuarios/editar_perfil.html',{'formulario':formulario})
    formulario = EdicionDatosUsuario(initial={'avatar':request.user.informacionextra.avatar,'descripcion':request.user.informacionextra.descripcion},instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

#Clase basa en vista parra modificar la contraseña, por eso que herede PasswordChangeView
class CambioContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasenia.html'
    success_url = reverse_lazy('editar_perfil')