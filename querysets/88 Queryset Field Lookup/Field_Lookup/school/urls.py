
from django.urls import path

from . import views 

urlpatterns = [

        # path('', views.home, name='home'),
        # path('<str:query>/', views.home, name='home'),
        # path('<str:start_date>/<str:end_date>/', views.home, name='home'),  # for range query 
        # path('<str:query>/', views.home, name='home'),  
        path('', views.home, name='home'),  
        
]