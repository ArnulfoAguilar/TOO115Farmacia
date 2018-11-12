# Nombre del archivo: urls.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/urls.py
# Objetivo: Proveer las urls de la aplicacion Farmacia

from django.urls import path
from . import views

urlpatterns = [
    # Pendiente index de farmacia (kendalalfonso37)
    path("", views.FarmaciaIndex.as_view(), name="farmacia_index"),
    #############################################################################################################
    # URLS Para los Tipos de Medicamentos
    # Autor: Kendal Sosa (kendalalfonso37)
    # Listar Tipos de Medicamentos
    path("tipo-medicamentos/list", views.TipoMedicamentoList.as_view(), name="tipo_medicamentos_list"),
    # Crear Tipo de Medicamento
    path("tipo-medicamentos/new", views.TipoMedicamentoCreate.as_view(), name="tipo_medicamentos_create"),
    # Editar Tipo de Medicamento
    path("tipo-medicamentos/edit/<int:pk>", views.TipoMedicamentoUpdate.as_view(), name="tipo_medicamentos_update"),
    # Eliminar Tipo de Medicamento
    path("tipo-medicamentos/delete/<int:pk>", views.TipoMedicamentoDelete.as_view(), name="tipo_medicamentos_delete"),

    #############################################################################################################
    # URLS Para los Presentacion de Medicamentos
    # Autor: Carlos  Moreno (charles9595)
    # Listar Presentacion de Medicamentos
    
    path("presentacion/list", views.PresentacionList.as_view(), name="presentacion_list"),
    # Crear Presentacion de Medicamento
    path("presentacion/new", views.PresentacionNew.as_view(), name="presentacion_new"),
    # Editar Presentacion de Medicamento
    path("presentacion/edit/<int:pk>", views.PresentacionUpdate.as_view(), name="presentacion_update"),
    # Eliminar Presentacion de Medicamento
    path("presentacion/delete/<int:pk>", views.PresentacionDelete.as_view(), name="presentacion_delete"),
    
]
