from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views

urlpatterns = patterns('',
    #url(r'^$', 'home.views.index'),	
	url(r'^$', include('home.urls', namespace="home")),
	url(r'^about/', include('about.urls', namespace="about")),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^projects/', include('projects.urls', namespace="projects")),
    url(r'^admin/', include(admin.site.urls)),
)