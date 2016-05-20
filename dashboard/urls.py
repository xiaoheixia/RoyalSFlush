from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$','dashboard.views.index',name='index'),
    url(r'^example$','dashboard.views.example',name='example'),
)
