

from django.urls import path

from . import views

urlpatterns = [
        path('', views.form_fields_examples, name='form_fields_examples'),
]
