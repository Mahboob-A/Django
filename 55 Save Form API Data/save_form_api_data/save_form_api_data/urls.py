

'''
031023, Tuesday, 08.30 am 
55 : Save From API Data in Django 
'''

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('form_fields_app.urls')),
]
