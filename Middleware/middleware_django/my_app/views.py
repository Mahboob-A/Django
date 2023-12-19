from django.shortcuts import render, HttpResponse

# Create your views here.

# view to test middleware 
def example_view(request): 
        print()
        print('example view is executed')
        print()
        return HttpResponse('this is example view response')

