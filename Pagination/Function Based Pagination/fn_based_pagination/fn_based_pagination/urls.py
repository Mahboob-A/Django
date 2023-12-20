
'''
071023, Saturday, 05.00 pm 
115: Function Based Pagination in Django 
'''


from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('general_app.urls')),
]
