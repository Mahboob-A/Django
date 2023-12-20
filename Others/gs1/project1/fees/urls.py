
from django.urls import path
from . import views 

urlpatterns = [
        path('fees_page/', views.fees_info, name='fees_info'), 
]
