

'''
250923, Monday, 08.00 pm 
50, 51, 52, 53: clean_field, clean, validators, password match 
'''

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
