# Nombre del archivo: views.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/views.py
# Objetivo: Proveer las vistas de la aplicacion Farmacia
from django.shortcuts import render, redirect

from django.urls import reverse_lazy,reverse
# Import de Vistas Basadas en Clases para los CRUD basicos
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import de Formularios
from .forms import TipoMedicamentoForm, MedicamentoForm, PresentacionForm, LoteForm, DescuentoForm
# Import de Modelos
from .models import TipoMedicamento, Medicamento, Presentacion, Lote, Descuento
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

#######################################################################################
# Vistas para el CRUD de Medicamentos
# Acciones: Crear, Actualizar, Eliminar, Listar, Detalles
# Autor: Kendal Sosa (kendalalfonso37)

class MedicamentoList(ListView):
    model = Medicamento
    template_name = "medicamento/medicamento_list.html"
    context_object_name = "medicamentos"
    paginate_by = 10

class MedicamentoDetail(DetailView):
    model = Medicamento
    template_name = "medicamento/medicamento_detail.html"
    context_object_name = "medicamento"

class MedicamentoCreate(CreateView):
    model = Medicamento
    form_class = MedicamentoForm
    success_url = reverse_lazy("medicamento_list")
    template_name = "medicamento/medicamento_new.html"

class MedicamentoUpdate(UpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    success_url = reverse_lazy("medicamento_list")
    template_name = "medicamento/medicamento_update.html"

class MedicamentoDelete(DeleteView):
    model = Medicamento
    success_url = reverse_lazy("medicamento_list")
    template_name = "medicamento/medicamento_delete.html"
    context_object_name = "medicamento"

#######################################################################################
# Vistas para la compra de lotes
# Acciones: Crear,Listar,
# Autor: Arnulfo Aguilar (ArnulfoAguilar)
def lote_add(request):
    if request.method   ==  'POST':
        
        form=LoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/farmacia/Lote/List')
    else:
        form = LoteForm()
    return render(request,'Farmacia/Lote/loteAdd.html',{'form' : form})

class loteList(ListView):
    model = Lote
    template_name = 'Farmacia/Lote/loteList.html'
    context_object_name = "lotes"
    paginate_by = 10 

#######################################################################################
# Vistas para CRUD Descuentos
# Acciones: Crear,Listar,
# Autor: Arnulfo Aguilar (ArnulfoAguilar)
#Vistas de Descuento
class DescuentoList(ListView):
    model = Descuento
    template_name = 'Farmacia/Descuento/DescuentoList.html'
    context_object_name = "descuentos"
    paginate_by = 10 

class DescuentoCreate(CreateView):
    model = Descuento
    form_class = DescuentoForm
    template_name = "Farmacia/Descuento/DescuentoCreate.html"
    success_url = reverse_lazy("descuento_List")