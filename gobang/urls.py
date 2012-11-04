from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'gobang.views.gobang_home'),
)

