from django.shortcuts import render

# Create your views here.


def home(request): 
        return render(request, 'cache_app/home.html')

def home2(request): 
        return render(request, 'cache_app/home2.html')