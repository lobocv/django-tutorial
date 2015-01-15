from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('mysite/index.html', context_instance=RequestContext(request))
	
def projects(request):
    return render_to_response('mysite/projects.html', context_instance=RequestContext(request))
	
def about(request):
    return render_to_response('mysite/about.html', context_instance=RequestContext(request))

def contact(request):
    return render_to_response('mysite/contact.html', context_instance=RequestContext(request))
		