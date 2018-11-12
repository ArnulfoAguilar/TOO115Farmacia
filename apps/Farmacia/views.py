# Nombre del archivo: views.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/views.py
# Objetivo: Proveer las vistas de la aplicacion Farmacia
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView
from .models import Lote
from .forms import LoteForm
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy

# Create your views here.
#class loteList(ListView):
 #   model= Lote 
  #  template_name= "Farmacia/Lote/loteList.html "



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