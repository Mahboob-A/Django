
from django.urls import path
from . import views

urlpatterns = [
        path('', views.example_view, name='example_view_for_middleware'), 
        path('view2/', views.example_view2, name='example_view_2_for_middleware'), 
        path('view3/', views.process_template_response_hook_view, name='process_template_response_hook_view'), 
]
