from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite import views

urlpatterns = patterns('',
    url(r'^$', 'mysite.views.index'),	
	url(r'^projects/', 'mysite.views.projects'),	
	url(r'^about/', 'mysite.views.about'),	
	url(r'^contact/', 'mysite.views.contact'),	
    url(r'^admin/', include(admin.site.urls)),
)
