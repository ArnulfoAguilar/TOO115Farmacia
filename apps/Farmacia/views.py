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
from .forms import TipoMedicamentoForm
# Import de Modelos
from .models import TipoMedicamento
# Create your views here.

# Farmacia Template View
class FarmaciaIndex(TemplateView):
    template_name = "farmacia/farmacia.html"


# Vistas para el CRUD de Tipos de Medicamentos
# Acciones: Crear, Actualizar, Eliminar, Listar
# Autor: Kendal Sosa (kendalalfonso37)
class TipoMedicamentoList(ListView):
    model = TipoMedicamento
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


