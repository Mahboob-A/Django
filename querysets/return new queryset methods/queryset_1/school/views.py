from django.shortcuts import render

# Create your views here.
from .models import Student 

def home(request): 
        # ALL : retuarns all the rows / objects of a table 
        students = Student.objects.all()
        
        # FILTER(**kwargs) :  returns only the rows matched with loopup param 
        # students = Student.objects.filter(name='Halim')
        
        # EXCLUDE(**kwargs) : returns those rows / objects that does not match with the given look up param 
        # students = Student.objects.exclude(marks=90)
        # students = Student.objects.exclude(marks=90, name='Jamal')  -> see why this way it doesnot work 
        
        # ORDER_BY(*fields)) : It orders by a 
        # students = Student.objects.order_by('?') --> given in random order in ascending 
        
        # REVERSE : It reverses the queryset. order_by must be set to use reverse 
        # students = Student.objects.order_by('name').reverse()   # it is again revrrsing the order to Desc 
        # students = Student.objects.order_by('name').reverse()[:5]  # slicing the result 
        
        # VALUES(*fields, **expressions) - returns a list of dict of all objects  
        # students = Student.objects.values() 
        # VALUES(fieldname, fieldname) - returns a list of dict of only the selected fields 
        # if we need all values of only some selected fields, then instead of using all(), use values()
        # students = Student.objects.values('name', 'roll') 
        
        # VALUES_LIST(*fields, flat=False, named=Flase)
        # students = Student.objects.values_list() # returns all the vlaues of the table as a list of touple 
        # students = Student.objects.values_list('id', 'name') # returns only the selected  vlaues of the table as a list of touple 
        # students = Student.objects.values_list('name', flat=True) # just a list of all the values of the fild 
        # students = Student.objects.values_list('id', 'name', 'marks', 'pass_date', named=True) # named touple, we can access like a dict 
        
        
        # students = Student.objects.values_list('id', 'name', 'marks', 'pass_date', named=True) 
        
        
        print("The Queryset : ",  students)
        print("SQL Query :  ",  students.query)
        return render(request, 'school/home.html', {'students' : students})