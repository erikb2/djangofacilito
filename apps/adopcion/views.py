from __future__ import absolute_import

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView # Vistas genericas
from django.core.urlresolvers import reverse_lazy

from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import AdopcionForm, SolicitudForm

# Create your views here.
def index(request):
    return HttpResponse("Hola Jefe. Estas en Index de Adopcion")

# Vistas para las Solicitudes
class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'
    context_object_name = 'lista_solicitudes'

class SolicitudCreate(CreateView):
    model = Solicitud
    form_class = SolicitudForm
    template_name = 'adopcion/solicitud_form.html'
    second_form_class = AdopcionForm
    success_url = reverse_lazy('adopcion:solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class SolicitudUpdate(UpdateView):
    model = Solicitud
    second_model = Persona
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = AdopcionForm
    success_url = reverse_lazy('adopcion:solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        persona   = self.second_model.objects.get(id=solicitud.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object
        id_solicitud = kwargs['pk']
        solicitud    = self.model.objects.get(id=id_solicitud)
        persona      = self.second_model.objects.get(id = solicitud.persona_id)
        form         = self.form_class(request.POST, instance = solicitud)
        form2        = self.second_form_class(request.POST, instance = persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'adopcion/solicitud_delete.html'
    context_object_name = 'solicitud'
    success_url = reverse_lazy('adopcion:solicitud_listar')
    

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