from django.shortcuts import render, HttpResponse

# Create your views here.

def create_exception(request): 
        error = 1/0 
        return HttpResponse()