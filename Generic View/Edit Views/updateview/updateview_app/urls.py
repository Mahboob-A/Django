from django.urls import path

from .views import StudentCreateView, ThankYouTemplateView,  SchoolStaffCreateView, SchoolStaffUpdateView, StudentUpdateView

urlpatterns = [
        
        # CreateViews 
        path('add/', StudentCreateView.as_view(), name='add_student'),
        path('staff/', SchoolStaffCreateView.as_view(), name='add_staff'),
        
        
        # UpdateViews 
        path('st-update/<int:pk>/', StudentUpdateView.as_view(), name='st_update'),
        path('staff-update/<int:pk>/', SchoolStaffUpdateView.as_view(), name='staff_update'),
        
        path('thank-you/', ThankYouTemplateView.as_view(), name='thank_you'),
        
]
