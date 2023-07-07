from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    name="ajsal"
    context={
        "name": name,
        
    }
    return render(request,"index.html",context=context)


def about(request):
    context={
    }
    return render(request,"about.html",context=context)
# Create your views here.
