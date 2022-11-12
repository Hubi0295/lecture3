from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def hubert(request):
    return HttpResponse("Helloooo Hubert")
def david(request):
    return HttpResponse("Helloooo david")
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize(),
        })