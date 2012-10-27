# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from django.template.context import RequestContext

def home(request):
    return render_to_response('home.html')
