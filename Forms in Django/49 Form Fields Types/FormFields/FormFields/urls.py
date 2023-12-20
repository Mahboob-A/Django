

'''
140923, Thursday, 08.00 pm 
49 : FormFields in Django 
'''

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('form_fields_app.urls')),
]
