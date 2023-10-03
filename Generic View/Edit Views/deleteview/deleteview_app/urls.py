from django.urls import path

from .views import StudentCreateView, ThankYouTemplateView,  SchoolStaffCreateView, StudentDeleteView

urlpatterns = [
        
        # CreateViews 
        path('add/', StudentCreateView.as_view(), name='add_student'),
        path('staff/', SchoolStaffCreateView.as_view(), name='add_staff'),
        
        # DeleteViews
        path('st-delete/<int:pk>/', StudentDeleteView.as_view(), name='del_student'),
        
        path('thank-you/', ThankYouTemplateView.as_view(), name='thank_you'),
        
]
