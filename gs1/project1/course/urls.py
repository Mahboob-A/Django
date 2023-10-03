
from django.urls import path
from . import views 

urlpatterns = [
    path('course_page/', views.course_info, name='course_info')
]
