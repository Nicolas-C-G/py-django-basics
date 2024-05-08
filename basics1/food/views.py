from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home(request):
    return render(request, 'index.html')

def item(request):
    return HttpRequest('<h1>This is an item</h1>')