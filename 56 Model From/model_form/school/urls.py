from django.urls import path
from .views import register_students


urlpatterns = [
        path('', register_students, name='student_registration'),
]
