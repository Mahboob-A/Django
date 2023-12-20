from django.shortcuts import render

# Create your views here.
from .models import Student
from datetime import date

def home(request, query=None, start_date=None, end_date=None): 
        # students = Student.objects.all()
        if query: 
        # if start_date: # for range query 
                # students = Student.objects.filter(name__exact=query)  # exact query WHERE "school_student"."name" = malim
                # students = Student.objects.filter(name__iexact=query)  # case insensitive uses WHERE LIKE query 
                # students = Student.objects.filter(name__contains=query)   # case sensitive matches any matching : WHERE "school_student"."name" LIKE %kala%
                # students = Student.objects.filter(name__icontains=query)  # case insensitive matches any matching with the query : WHERE "school_student"."name" LIKE %hali%
                # students = Student.objects.filter(name__icontains=query)  # case insensitive matches any matching with the query : WHERE "school_student"."name" LIKE %hali%
                # students = Student.objects.filter(marks__in=[query])  # here, we need to pass a list or tuples (in query pass the marks, and it will return if any marks with the passed values are matched)
                # students = Student.objects.filter(marks__gt=query)  # gt is greater than | WHERE "school_student"."marks" > 50
                # students = Student.objects.filter(marks__gte=query)  # gt is greater than equal to | WHERE "school_student"."marks" >= 50
                # students = Student.objects.filter(marks__lt=query)  # lt is less than  | WHERE "school_student"."marks" < 50
                # students = Student.objects.filter(marks__lte=query)  # lte is less than equal to | WHERE "school_student"."marks" <= 50
                # students = Student.objects.filter(name__startswith=query)  # case sensetive , checks matching object starting with query | WHERE "school_student"."name" LIKE s%
                # students = Student.objects.filter(name__istartswith=query)  # case insensetive , checks matching object starting with query |  WHERE "school_student"."name" LIKE j%
                # students = Student.objects.filter(name__endswith=query)  # case sensetive , checks matching matching object ending with query |  WHERE "school_student"."name" LIKE %n
                # students = Student.objects.filter(name__iendswith=query)  # case insensetive , checks matching matching object ending with query |  WHERE "school_student"."name" LIKE %l
                
                # for range query 
                students = Student.objects.filter(pass_date__range=(start_date, end_date))  # pass_date__range=('2023-5-4', '2023-9-5) date format is => yyyy-mm-dd |  WHERE "school_student"."pass_date" BETWEEN 2023-02-03 AND 2023-10-05
                
                # for date query | date query only works in DateTimeField only. 
        # students = Student.objects.filter(admission_date__date__gt=date(2023, 1, 4))   # format => date(yyyy, mm, dd)  date(2023, 5, 3) |
        else: 
                students = Student.objects.all()

        print("Return : ", students)
        print()
        print("SQL Query: ", students.query)
        return render(request, 'school/home.html', {'students' : students})
