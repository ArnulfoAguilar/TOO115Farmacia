# Nombre del archivo: admin.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/admin.py
# Objetivo: Proveer los modelos que administrara el sitio del Administrador de Django

from django.contrib import admin
# Modelos para importar en el proyecto que manejara el admin de Django
from django.contrib.auth.admin import UserAdmin
from .models import User, Rol, Empresa

# Customizacion del UserAdmin para poder Ingresar Rol y Empresa en el Admin
# Nota: Ambos campos deben ser obligatorios, por tanto debe crearse una empresa y un rol al menos o no guardara nada
class MyUserAdmin(UserAdmin):
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('id_rol', 'id_empresa')}),
		)

# Registramos nuestro modelo User Customizado
admin.site.register(User, MyUserAdmin)

# Registramos los demas modelos que usara el Administrador
admin.site.register(Rol)
admin.site.register(Empresa)