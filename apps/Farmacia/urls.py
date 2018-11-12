# Nombre del archivo: urls.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/urls.py
# Objetivo: Proveer las urls de la aplicacion Farmacia

from django.urls import path
from django.conf.urls import url, include
from .views import lote_add, loteList

urlpatterns=[
    
    path("Lote/add", lote_add, name="lote_create"),
    path("Lote/List", loteList.as_view(), name="lote_List"),
]