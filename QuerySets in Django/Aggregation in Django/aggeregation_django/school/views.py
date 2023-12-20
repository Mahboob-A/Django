from django.shortcuts import render

from django.db.models import Avg, Sum, Min, Max, Count, Manager, ManyToOneRel

from .models import Student



def home(request): 
        
        ''' 
        limiting queryset : if silicing has either stop or start and stop, then it returns a queryset. 
        here, SQL LIMIT and OFFSET is used. 
        
        Example SQL Query : 
        SELECT "school_student"."id", "school_student"."name", 
        "school_student"."roll", "school_student"."grade", "school_student"."city", "school_student"."marks", 
        "school_student"."admission_date", "school_student"."pass_date" 
        FROM "school_student" LIMIT 4 OFFSET 3
        '''
        
        students = Student.objects.all()[3:7]
        
        
        
        
        ''' 
        limiting queryset | the below start : end : step slicing returns a list, not queryset. so, this student is a list, so no ORM 
        activiting would work here. 
        '''
        # students = Student.objects.all()[3:7:2]
        
        
        print('student type: ', type(students))

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

        
        
        print("Queryset : ", students)
        print()
        print("SQL Query: ", students.query)
        return render(request, 'school/home.html', context)
