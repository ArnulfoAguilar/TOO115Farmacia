# Nombre del archivo: views.py
# Direccion Fisica: TOO115Farmacia/apps/usuarios/views.py
# Objetivo: Proveer las vistas de la aplicacion usuarios y el index del sitio
from django.shortcuts import render, redirect
#juanjo:importaremos las clases qeu nos proporcionan djanfgo para poder
#listar eliminar.....CRUD
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
#END JUANJO
# Modulos para autenticacion e inicio de sesion
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from apps.Farmacia.models import Kardex
User = get_user_model()
# Import de Formularios
from .forms import SignUpForm
# Import de Modelos
from apps.Farmacia.models import Rol
#juanjo :importar el modelo user
from apps.Farmacia.models import User


# import de Views



# Nombre de la vista: index
# Direccion fisica: TOO115Farmacia/apps/usuarios/views.py
# Objetivo: Proveer el indice del sistema informatico
def index(request):
	kardex = Kardex.objects.all()
	for kar in kardex:
		transac= kar.id_transaccion

	return render(request, 'index.html',
	{
		'kardex' : kardex,
		'transaccion' : transac
	})
# Nombre de la vista: sign_up
# Direccion fisica: TOO115Farmacia/apps/usuarios/views.py
# Objetivo: Proveer un formulario para que los usuarios puedan registrarse en el sistema
def sign_up(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			# Guardamos el Usuario
			form.save()
			# Obtenemos datos del usuario
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			# Autenticamos el usuario e iniciamos sesion
			user = authenticate(request, username=username, password=raw_password)
			login(request, user)
			return redirect(index)
	else:
		form = SignUpForm()
		# redirigir el formulario vacio para llenar los datos
	return render(request, 'usuarios/signup.html', {'form': form})

# Create your views here.



#JUANJO: clase para listar los bodegueros
class BodegueroListView(ListView):
    model=User