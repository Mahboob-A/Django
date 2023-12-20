from django.shortcuts import render

from django.db.models import Avg, Sum, Min, Max, Count, Manager, ManyToOneRel

from .models import Student



def home(request): 
        
        students = Student.objects.all()

        # aggregatoin classes 
        avg_marks = students.aggregate(Avg('marks'))
        total_marks_sum = students.aggregate(Sum('marks'))
        min_marks = students.aggregate(Min('marks'))
        max_marks = students.aggregate(Max('marks'))
        total_marks_count = students.aggregate(Count('marks'))
        
        context = {
                'students' : students,
                 
                # aggregation results 
                'avg_marks' : avg_marks, 
                'total_marks_sum' : total_marks_sum, 
                'min_marks' : min_marks, 
                'max_marks' : max_marks, 
                'total_marks_count' : total_marks_count
        }

        print("Return : ", students)
        print()
        print("SQL Query: ", students.query)
        return render(request, 'school/home.html', context)
