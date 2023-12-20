from django.shortcuts import render

# Create your views here.
def course_info(request):
        return render(request, 'course/course_info.html', {'page' : 'course_info'})