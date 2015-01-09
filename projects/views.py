from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index(request):
	return render_to_response('projects/index.html', context_instance=RequestContext(request))