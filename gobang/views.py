# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from django.template.context import RequestContext

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

def gobang_home(request):
    context = RequestContext(request)
    return render_to_response('gobang_home.html', context)
