from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, Guys!")

def riaz(request):
    context = {}
    context['hello'] = 'Hello Riaz!'
    return render(request, 'display.html',context)