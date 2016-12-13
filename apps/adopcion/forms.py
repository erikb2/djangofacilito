from __future__ import absolute_import
from django import forms

from apps.adopcion.models import Persona, Solicitud

class AdopcionForm(forms.ModelForm):

    class Meta:
        model = Persona
        # Aqui se senalan los campos que nos traemos
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'domicilio',
        ]

        # Etiqueta de cada campo
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'domicilio': 'Domicilio',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
        }


class SolicitudForm(forms.ModelForm):
    model = Solicitud
    fields = [
        'numero_mascotas',
        'razones',
    ]

    labels = {
        'numero_mascotas': 'Numero de mascotas',
        'razones': 'Razones para adoptar',
    }

    widgets = {
        'numero_mascotas': forms.TextInput(attrs={'class':'form-control'}),
        'razones':forms.TextArea(attrs={'class':'form-control'}),
    }
