from django.shortcuts import render             #importing renderer support
from django.http import HttpResponse            #importing html support

# Create your views here.

def home(request):
    return render(request, 'index.html')

def addition(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result=val1 + val2
    return render(request,'result.html',{'result':result})