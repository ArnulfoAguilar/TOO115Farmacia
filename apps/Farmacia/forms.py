# Nombre del archivo: forms.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/forms.py
# Objetivo: Proveer los formularios del proyecto Farmacia
from django import forms
from .models import Lote

class LoteForm(forms.ModelForm):
    class Meta():
        model = Lote
        fields = [
            
            'id_medicamento',
            'id_empresa',
            'fecha_compra',
            'cantidad',
            ]
        labels={
           
            'id_medicamento' : 'Medicamento',
            'id_empresa': 'Empresa',
            'fecha_compra' : 'Fecha',
            'cantidad' : 'Cantidad',
        }
        widgets ={
            
            'id_medicamento' : forms.Select(attrs={'class':'form-control', "required": True}),
            'id_empresa': forms.Select(attrs={'class':'form-control', "required": True}),
            'fecha_compra': forms.DateInput(attrs={'class':'form-control', "required": True}),
            'cantidad' : forms.NumberInput(attrs={'class':'form-control', "required": True}),
        }
       