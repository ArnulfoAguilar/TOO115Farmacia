# Nombre del archivo: views.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/views.py
# Objetivo: Proveer las vistas de la aplicacion Farmacia
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Import de Vistas Basadas en Clases para los CRUD basicos
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import de Formularios
from .forms import TipoMedicamentoForm, PresentacionForm
# Import de Modelos
from .models import TipoMedicamento, Presentacion
# Create your views here.

# Farmacia Template View
class FarmaciaIndex(TemplateView):
    template_name = "farmacia/farmacia.html"

#######################################################################################
# Vistas para el CRUD de Tipos de Medicamentos
# Acciones: Crear, Actualizar, Eliminar, Listar
# Autor: Kendal Sosa (kendalalfonso37)
class TipoMedicamentoList(ListView):
    model = TipoMedicamento #recordar importar modelo de TipoMedicamento
    template_name = "tipo_medicamento/tipo_medicamento_list.html"
    context_object_name = "tipo_medicamentos"
    paginate_by = 10

class TipoMedicamentoCreate(CreateView):
    model = TipoMedicamento
    form_class = TipoMedicamentoForm
    success_url = reverse_lazy("tipo_medicamentos_list")
    template_name = "tipo_medicamento/tipo_medicamento_new.html"

class TipoMedicamentoUpdate(UpdateView):
    model = TipoMedicamento
    form_class = TipoMedicamentoForm
    success_url = reverse_lazy("tipo_medicamentos_list")
    template_name = "tipo_medicamento/tipo_medicamento_update.html"

class TipoMedicamentoDelete(DeleteView):
    model = TipoMedicamento
    success_url = reverse_lazy("tipo_medicamentos_list")
    template_name = "tipo_medicamento/tipo_medicamento_delete.html"
    context_object_name = "tipo_medicamentos"

#######################################################################################
# Vistas para el CRUD de PRESENTACIONES
# Acciones: Crear, Actualizar, Eliminar, Listar
# Autor: Carlos  Moreno (charles9595)
class PresentacionList(ListView):
    model = Presentacion #recordar importar modelo de presentacion
    template_name = "presentacion/presentacion_list.html"
    context_object_name = "presentaciones"
    paginate_by = 10

class PresentacionNew(CreateView):
    model = Presentacion
    form_class = PresentacionForm
    success_url = reverse_lazy("presentacion_list")
    template_name = "presentacion/presentacion_new.html"

class PresentacionUpdate(UpdateView):
    model = Presentacion
    form_class = PresentacionForm
    success_url = reverse_lazy("presentacion_list")
    template_name = "presentacion/presentacion_update.html"

class PresentacionDelete(DeleteView):
    model = Presentacion
    success_url = reverse_lazy("presentacion_list")
    template_name = "presentacion/presentacion_delete.html"
    context_object_name = "presentacion"