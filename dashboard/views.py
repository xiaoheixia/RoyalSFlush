# coding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.template import Context,Template
from django.views.generic import TemplateView

def index(request):
    return render_to_response('index.html')

def example(request):
    return render_to_response('example.html')