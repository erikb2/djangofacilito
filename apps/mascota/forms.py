from __future__ import absolute_import
from django import forms

from apps.mascota.models import Mascota
# Obtenemos el formulario de acuerdo al modelo que
# seleccionamos
class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota
        # Aqui se senalan los campos que nos traemos
        fields = [
            'nombre',
            'sexo',
            'edad',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]

        # Aqui senalamos la etiqueta de cada campo 
        # que nos vamos a traer
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad': 'Edad Aprox.',
            'fecha_rescate': 'Fecha de Rescate',
            'persona': 'Adoptante',
            'vacuna': 'Vacunas',
        }

        # Son los que se van a pintar a forma de etiquetas
        # en html
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }