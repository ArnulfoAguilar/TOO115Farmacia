from django.shortcuts import render, redirect
# Modulos para autenticacion e inicio de sesion
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
User = get_user_model()
# Import de Formularios
from .forms import SignUpForm
# Import de Modelos

# Create your views here.

def index(request):
	return render(request, 'index.html')

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
		# redirigir el formulario vacio para volver a llenar
	return render(request, 'signup/signup.html', {'form': form})
