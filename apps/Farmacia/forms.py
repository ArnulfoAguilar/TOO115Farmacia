# Nombre del archivo: forms.py
# Direccion Fisica: TOO115Farmacia/apps/Farmacia/forms.py
# Objetivo: Proveer los formularios del proyecto Farmacia
from django import forms

# Import de Modelos
from .models import TipoMedicamento

# Crear Formularios aqui
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
