# Nombre del archivo: urls.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/urls.py
# Objetivo: Proveer las urls de la aplicacion Farmacia

from django.urls import path
from . import views

urlpatterns = [
    # Pendiente index de farmacia (kendalalfonso37)
    path("", views.FarmaciaIndex.as_view(), name="farmacia_index"),
    
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

    # URLS Para los Medicamentos
    # Autor: Kendal Sosa (kendalalfonso37)
    # Listar Tipos de Medicamentos
    path("medicamento/list", views.MedicamentoList.as_view(), name="medicamento_list"),
    # Detalle de Medicamento
    path("medicamento/info/<int:pk>", views.MedicamentoDetail.as_view(), name="medicamento_detail"),
    # Crear Tipo de Medicamento
    path("medicamento/new", views.MedicamentoCreate.as_view(), name="medicamento_create"),
    # Editar Tipo de Medicamento
    path("medicamento/edit/<int:pk>", views.MedicamentoUpdate.as_view(), name="medicamento_update"),
    # Eliminar Tipo de Medicamento
    path("medicamento/delete/<int:pk>", views.MedicamentoDelete.as_view(), name="medicamento_delete"),
]
