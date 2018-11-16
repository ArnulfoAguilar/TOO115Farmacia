# Nombre del archivo: forms.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/forms.py
# Objetivo: Proveer los formularios del proyecto Farmacia
# Import de Modelos
from django import forms
from .models import TipoMedicamento, Medicamento, Presentacion, Lote, Descuento

# Crear Formularios aqui-------------------------------------------------------------------
#Formulario para los TIPOS DE MEDICAMENTOS  ###############################################
class TipoMedicamentoForm(forms.ModelForm):
    class Meta():
        model = TipoMedicamento
        fields = ['tipo',]
        labels = {
            'tipo': "Ingrese el Tipo de Medicamento (Por su uso o efectos secundarios):"
        }
        widgets = {
            'tipo': forms.TextInput(attrs={"class": "form-control", "required": True})
        }

class MedicamentoForm(forms.ModelForm):
    class Meta():
        model = Medicamento
        fields = ['id_presentacion', 'id_tipo', 'nombre', 'precio']
        labels = {
            'id_presentacion': "Presentacion del Medicamento",
            'id_tipo': "Tipo de Medicamento",
            'nombre': "Nombre del Medicamento",
            'precio': "Precio del Medicamento",
        }
        widgets = {
            'id_presentacion': forms.Select(choices=Presentacion.objects.all(), attrs={"class": "form-control", "required": True}),
            'id_tipo': forms.Select(choices=TipoMedicamento.objects.all(), attrs={"class": "form-control", "required": True}),
            'nombre': forms.TextInput(attrs={"class": "form-control", "required": True}),
            'precio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'value': '0', "type": "number", "min": 0, "step":".01", "lang": "en"})
        }

# formulario  para las PRESENTACIONES DE MEDICAMENTOS    ##################################################
class PresentacionForm(forms.ModelForm):
    class Meta():
        model = Presentacion
        fields = ['presentacion',]
        labels = {
            'presentacion': "Ingrese la Presentacion del Medicamento:"
        }
        widgets = {
            'presentacion': forms.TextInput(attrs={"class": "form-control", "required": True})
        }
# formulario  para la compra de Lotes de medicamento    ##################################################
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

# formulario  para Crear Descuentos    ##################################################
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