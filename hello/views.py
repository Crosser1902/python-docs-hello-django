from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, Guys!")

def riaz(request):
    context = {}
    context['hello'] = 'Hello Riaz!'
    return render(request, 'display.html',context)

def runoob(request):
    views_name = ["Rookie1","Rookie2","Rookie3"]
    return render(request, 'runoob.html',{"views_list":views_name})

















