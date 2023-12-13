from django.shortcuts import render

# Create your views here.

# we can also use caching here using cache_app decorator but if we implement cache on directly on view, 
# then all the endponts will be cached. so, caching in url conf is better as we can create cached and non cahced enpoint 
# directly in the url conf. 
def home(request): 
        return render(request, 'cache_app/home.html')

def contact(request): 
        return render(request, 'cache_app/contact.html')