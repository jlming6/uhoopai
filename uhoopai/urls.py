from django.conf.urls import patterns, include, url

from django.contrib.auth.views import login, logout

import os

static = os.path.join(os.path.dirname(__file__), 'static')

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uhoopai.views.home', name='home'),
    # url(r'^uhoopai/', include('uhoopai.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'uhoopai.views.home', name="mainPage"),

    (r'accounts/', include('registration.backends.default.urls')),

    url(r'^gobang/', include('gobang.urls')),

    # Site Media

    (r'^static/(?P<path>.*)$', 'django.views.static.serve'),
)
