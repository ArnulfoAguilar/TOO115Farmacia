# Nombre del archivo: urls.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/urls.py
# Objetivo: Proveer las urls de la aplicacion Farmacia

from django.urls import path
from django.conf.urls import url, include
from . import views
#from .views import lote_add, loteList, DescuentoList, DescuentoCreate

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

     #############################################################################################################
      # URLS Para compra de Lotes
    # Autor: Arnulfo Aguilar (ArnulfoAguilar)
     # Comprar Lote de Medicamento
    path("Lote/add", views.lote_add, name="lote_create"),
     # Listar Lote de Medicamento
    path("Lote/List", views.loteList.as_view(), name="lote_List"),

#############################################################################################################
      # URLS Para manejar descuentos
    # Autor: Arnulfo Aguilar (ArnulfoAguilar)
     # Listar Descuentos
    path("Descuento/List", views.DescuentoList.as_view(), name="descuento_List"),
     # Agregar nuevo descuento
    path("Descuento/Create", views.DescuentoCreate.as_view(), name="descuento_Create"),

    # URLS para proceso de Venta de Medicamentos
    path('venta/', views.VentaTemplate.as_view(), name='venta'),
    path('api/obtener_medicamentos', views.obtener_medicamentos, name="api_obtener_medicamentos"),
    path('api/seleccionar_medicamento', views.seleccionar_medicamento, name="api_seleccionar_medicamento")
]