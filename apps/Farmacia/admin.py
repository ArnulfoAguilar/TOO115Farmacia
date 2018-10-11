from django.contrib import admin
# Modelos para importar en el proyecto que manejara el admin de Django
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)