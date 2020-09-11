from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def bryan(request):
    return HttpResponse("Hola Bryan!")

def david(request):
    return HttpResponse("Hola David!")

def greet(request, name):
    return render(request,"hello/greet.html",{
        "name":name.capitalize()
    })
