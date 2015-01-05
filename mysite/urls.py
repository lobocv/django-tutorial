from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views

urlpatterns = patterns('',
    url(r'^$', 'home.views.index'),
	url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)