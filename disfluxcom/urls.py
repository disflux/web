from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    #url(r'^disfluxcom/', include('disfluxcom.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
