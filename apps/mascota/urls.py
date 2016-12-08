from __future__ import absolute_import
from django.conf.urls import url
from django.core.urlresolvers import reverse
from apps.mascota.views import index

urlpatterns = [
    url(r'^$', index, name="Index"),
]