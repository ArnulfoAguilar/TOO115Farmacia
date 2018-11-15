# Nombre del archivo: views.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/views.py
# Objetivo: Proveer las vistas de la aplicacion Farmacia
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView
from .models import Lote, Descuento
from .forms import LoteForm, DescuentoForm
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy

# Create your views here.
#class loteList(ListView):
 #   model= Lote 
  #  template_name= "Farmacia/Lote/loteList.html "


#Vistas de Lotes
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