

'''
031023, Tuesday, 08.30 am 
56 : Model Form in Django 
'''

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('school.urls')),
]
