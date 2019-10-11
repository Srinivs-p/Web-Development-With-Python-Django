from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request,'index.html')

def generic(request):
    return render(request,'generic.html')

def resume_page(request):
    return render(request,'elements.html')