# Nombre del archivo: forms.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/forms.py
# Objetivo: Proveer los formularios del proyecto Farmacia
from django import forms
from .models import Lote, Descuento

class LoteForm(forms.ModelForm):
    class Meta():
        model = Lote
        fields = [
            
            'id_medicamento',
            'id_empresa',
            'fecha_compra',
            'cantidad',
            'precio_unitario',
            ]
        labels={
           
            'id_medicamento' : 'Medicamento',
            'id_empresa': 'Empresa',
            'fecha_compra' : 'Fecha',
            'cantidad' : 'Cantidad',
            'precio_unitario' : 'Precio Unitario',
        }
        widgets ={
            
            'id_medicamento' : forms.Select(attrs={'class':'form-control', "required": True}),
            'id_empresa': forms.Select(attrs={'class':'form-control', "required": True}),
            'fecha_compra': forms.DateInput(attrs={'class':'form-control', "required": True}),
            'cantidad' : forms.NumberInput(attrs={'class':'form-control', "required": True}),
            'precio_unitario' : forms.NumberInput(attrs={'class':'form-control', "required": True}),
        }

class DescuentoForm(forms.ModelForm):
    class Meta():
        model = Descuento
        fields = [
            'id_descuento',
            'nombre' ,
            'field_desc',
            'fecha_inicio' ,
            'fecha_fin' ,
            ]
        labels={
           
            'id_descuento' : 'ID',
            'nombre' : 'Nombre',
            'field_desc' : 'Porcentaje',
            'fecha_inicio' : 'Fecha de Inicio',
            'fecha_fin' : 'Fecha de Fin',
        }
        widgets ={

            'nombre' : forms.TextInput(attrs={'class':'form-control', "required": True}) ,
            'field_desc' : forms.NumberInput(attrs={'class':'form-control', "required": True}),
            'fecha_inicio' : forms.DateInput(attrs={'class':'form-control', "required": True}) ,
            'fecha_fin' : forms.DateInput(attrs={'class':'form-control', "required": True}),
          
        }
       