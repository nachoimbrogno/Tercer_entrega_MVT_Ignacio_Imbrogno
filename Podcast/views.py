from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
# Create your views here.

def mi_vista(request):
    # return HttpResponse ("<h1>Mi primera vista</h1>")
    return render(request,'Podcast/index.html',)
