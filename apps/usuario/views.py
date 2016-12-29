from __future__ import absolute_import

import json
from rest_framework.views import APIView

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse


from apps.usuario.forms import RegistroForm
from apps.usuario.serializers import UserSerializer

# Esta clase es la Default para las Formas de User.
'''class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('mascota:mascota_listar')'''

# Esta clase es utilizando un Forms creado por nosotros y Hereda de User
class RegistroUsuario(CreateView):
    model         = User
    template_name = "usuario/registrar.html"
    form_class    = RegistroForm
    success_url   = reverse_lazy("mascota:mascota_listar")

class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')
