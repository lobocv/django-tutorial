from django.conf.urls import patterns, url

urlpatterns = patterns('',
		url(r'^$', 'home.views.index'))
		#url(r'^about/', 'about.views.about'))
		