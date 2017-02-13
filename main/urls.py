from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    list,
    detail,
    create,
)


urlpatterns = [
    url(r'^$', list),
    url(r'(?P<id>\d+)/$', detail, name='detail'),
    url(r'^create/$', create)
]


