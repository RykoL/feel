from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "journal/index.html")

def feeling_good(request):
    return render(request, "journal/feelings/good.html")
