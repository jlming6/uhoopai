# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from django.template.context import RequestContext

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()

    context = RequestContext(request)
    context['form'] = form
    return render_to_response("registration/register.html", context)

