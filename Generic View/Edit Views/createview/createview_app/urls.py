
from django.urls import path

from .views import StudentCreateView,ThankYouTemplateView, StudentDetailView, TeacherCreateView, SchoolStaffCreateView

urlpatterns = [
        path('add/', StudentCreateView.as_view(), name='add_student'),
        path('add/thank-you/', ThankYouTemplateView.as_view(), name='thank_you'),
        path('add/thank-you/<int:pk>/', StudentDetailView.as_view(), name='detail'),
        
        # teachercreateview
        path('teacher/', TeacherCreateView.as_view(), name='add_teacher'),
        
        # school staff create view (using model form)
        path('staff/', SchoolStaffCreateView.as_view(), name='add_staff'),
        
]
