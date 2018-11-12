"""TOO115Farmacia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Urls para el sitio de Administracion de Django
    path('admin/', admin.site.urls),
    # Url para el index de la pagina. (La vista esta en apps.usuarios.views)
    path('', RedirectView.as_view(url='/usuarios/index/'), name='index'),
    # Urls para la aplicacion Farmacia (Donde estara toda la logica de nuestro proyecto)
    #path('farmacia/',include('apps.Farmacia.urls')),
    # Urls para la parte de los Usuarios (Donde manejaremos la parte de los usuarios)
    path('usuarios/', include('apps.usuarios.urls')),
    path('farmacia/', include('apps.Farmacia.urls')),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
