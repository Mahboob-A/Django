
from django.urls import path 


from . import views 

urlpatterns = [

        path('', views.home, name='home'), # cache in template 
        path('contanct/', views.contact, name='contact'),
        
]

# cache_page(60 * 15)(my_view)),  => cache_app takes time in secconds 