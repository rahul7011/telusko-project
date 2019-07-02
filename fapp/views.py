from django.shortcuts import render             #importing renderer support
from django.http import HttpResponse            #importing html support

# Create your views here.

def home(request):
    return HttpResponse('Hello World!')
