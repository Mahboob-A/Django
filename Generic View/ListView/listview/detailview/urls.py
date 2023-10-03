# 100723, Monday, 06.15 am 


from django.urls import path 
from .views import TeacherDetailView, GeneralListView, SubjectTeacherListView

urlpatterns = [
        path('<int:pk>/', TeacherDetailView.as_view(), name='teacherdetail'),
        path('', GeneralListView.as_view(), name='show_teacher_data'),
        path('<str:sub>/', SubjectTeacherListView.as_view(), name='subject_teacher_list'),
]

