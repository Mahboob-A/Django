
from django.urls import path 
from django.views.decorators.cache import cache_page

from . import views 

urlpatterns = [

        path('', views.home, name='home'), # this endpoint is not cached i.e. this endpoint will be rendered real time 
        path('home/', cache_page(30)(views.home), name='cached_home'), # this endpont got the same view is cached. 
        path('contanct/', views.contact, name='contact'),
        
]

# cache_page(60 * 15)(my_view)),  => cache_app takes time in secconds 