"""
URL configuration for crud2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

'''
watch date begin : 070723, Friday, 11.30 am 
watch end date : 
Video no : 101 CRUD project 2 using class based views 
'''

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('enroll.urls')),
]





# from enroll import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.add_show, name="addandshow"),
#     path('delete/<int:id>/', views.delete_data, name="deletedata"),
#     path('<int:id>/', views.update_data, name="updatedata"),
# ]

