# Nombre del archivo: forms.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/forms.py
# Objetivo: Proveer los formularios del proyecto Farmacia
from django import forms

# Import de Modelos
from .models import TipoMedicamento
from .models import Presentacion

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