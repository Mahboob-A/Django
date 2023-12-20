
"""
Geeky Shows || Vid 34 - Retrive Values form database and show in tmplate 
120623, Monday, 04.30 pm 
"""

from django.shortcuts import render

# from course.models import Student
from .models import Student   #.couse means from this current directory 

# Create your views here.
def student_info(request):
        st_info = Student.objects.all()
        return render(request, 'course/student_info.html', {'st_info' : st_info})
