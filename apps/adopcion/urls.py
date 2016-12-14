from __future__ import absolute_import
from django.conf.urls import url

from apps.adopcion.views import index, AdopcionList, AdopcionCreate, AdopcionUpdate, AdopcionDelete, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    url(r'^$', index, name="Index"),
    url(r'^nuevo$', AdopcionCreate.as_view(), name='adopcion_crear'),
    url(r'^listar$', AdopcionList.as_view(), name= "adopcion_listar"),
    url(r'^editar/(?P<pk>\d+)/$', AdopcionUpdate.as_view(), name="adopcion_editar"),
    url(r'^eliminar/(?P<pk>\d+)/$', AdopcionDelete.as_view(), name="adopcion_eliminar"),
    # Solicitudes
    url(r'^solicitud/listar$', SolicitudList.as_view(), name="solicitud_listar"),
    url(r'^solicitud/nueva$', SolicitudCreate.as_view(), name="solicitud_crear"),
    url(r'^solicitud/editar/(?P<pk>\d+)$', SolicitudUpdate.as_view(), name="solicitud_editar"),
    url(r'^solicitud/eliminar/(?P<pk>\d+)$', SolicitudDelete.as_view(), name="solicitud_eliminar"),
]