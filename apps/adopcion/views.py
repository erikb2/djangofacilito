from __future__ import absolute_import

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView # Vistas genericas
from django.core.urlresolvers import reverse_lazy

from apps.adopcion.models import Persona
from apps.adopcion.forms import AdopcionForm

# Create your views here.
def index(request):
    return HttpResponse("Hola Jefe. Estas en Index de Adopcion")


# Vista basada en clase
# para el listado de los adoptantes
class AdopcionList(ListView):
    model = Persona
    template_name = 'adopcion/adopcion_list.html'
    queryset = Persona.objects.order_by('id')

class AdopcionCreate(CreateView):
    model = Persona
    form_class = AdopcionForm
    template_name = 'adopcion/adopcion_form.html'
    success_url = reverse_lazy('adopcion:adopcion_listar')

class AdopcionUpdate(UpdateView):
    model = Persona
    form_class = AdopcionForm
    template_name = 'adopcion/adopcion_form.html'
    success_url = reverse_lazy('adopcion:adopcion_listar')

class AdopcionDelete(DeleteView):
    model = Persona
    template_name = 'adopcion/adopcion_delete.html'
    context_object_name = 'adopcion' # Se envia el objeto con el nombre de adopcion
    success_url = reverse_lazy('adopcion:adopcion_listar')