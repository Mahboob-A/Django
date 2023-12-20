

'''
031023, Tuesday, 08.30 am 
54 : Form Field Errors in Django 
'''

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('form_fields_app.urls')),
]
