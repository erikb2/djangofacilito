from __future__ import absolute_import
from django.conf.urls import url

from apps.adopcion.views import index, AdopcionList, AdopcionCreate, AdopcionUpdate, AdopcionDelete

urlpatterns = [
    url(r'^$', index, name="Index"),
    url(r'^nuevo$', AdopcionCreate.as_view(), name='adopcion_crear'),
    url(r'^listar$', AdopcionList.as_view(), name= "adopcion_listar"),
    url(r'^editar/(?P<pk>\d+)/$', AdopcionUpdate.as_view(), name="adopcion_editar"),
    url(r'^eliminar/(?P<pk>\d+)/$', AdopcionDelete.as_view(), name="adopcion_eliminar"),
]