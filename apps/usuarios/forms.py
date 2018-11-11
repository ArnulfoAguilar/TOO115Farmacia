# Nombre del archivo: forms.py
# Direccion Fisica: TOO115Farmacia/apps/usuarios/forms.py
# Objetivo: Proveer los formularios de la aplicacion usuarios
from django import forms
# Imports para crear el formulario de Registro de usuario
from django.contrib.auth.forms import UserCreationForm

# Crear un objeto de tipo usuario
from django.contrib.auth import get_user_model
User = get_user_model()

# Formulario para Registrar Usuario
class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Ingrese su Nombre.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Ingrese Apellidos.')
	email = forms.EmailField(max_length=254, help_text='Ingrese un correo valido.')

	class Meta:
		model = User
		
		fields = (
			'username',	
			'first_name', 
			'last_name', 
			'password1', 
			'password2',
		)
		
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, *kwargs)
		self.fields['username'].widget.attrs.update({'class':'form-control'}),
		self.fields['first_name'].widget.attrs.update({'class' : 'form-control'}),
		self.fields['last_name'].widget.attrs.update({'class' : 'form-control' }),
		self.fields['email'].widget.attrs.update({'class' : 'form-control' }),
		self.fields['password1'].widget.attrs.update({'class' : 'form-control' }),
		self.fields['password2'].widget.attrs.update({'class' : 'form-control' }),
			