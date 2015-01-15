from django.shortcuts import render, render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('mysite/index.html',
                              {'page_title': 'The Wolf Den'},
                              context_instance=RequestContext(request))


def projects(request):
    return render_to_response('mysite/projects.html',
                              {'page_title': 'Projects'},
                              context_instance=RequestContext(request))


def about(request):
    return render_to_response('mysite/about.html',
                              {'page_title': 'About'},
                              context_instance=RequestContext(request))


def contact(request):
    return render_to_response('mysite/contact.html',
                              {'page_title': 'Contact'},
                              context_instance=RequestContext(request))
		