
from django.urls import path 
from . import views 

urlpatterns = [
        path('show-form/', views.show_form, name='show-form-link'),
        path('show-form-2/', views.show_form_2, name='show-form-2-link'),
        path('show-form-widget/', views.show_form_widget, name='show_form_widget_link'),
        path('show-data/', views.show_enroll_data, name='show-data-link'),
        
]
