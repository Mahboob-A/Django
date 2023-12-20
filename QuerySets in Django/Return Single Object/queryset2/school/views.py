from django.shortcuts import render

# Create your views here.
from .models import Student 

'''
these methods only returns a single object, rather than a queryset. 
'''
def home(request): 

        ##### GET : get(pk, id)
        # - retruns the single matching object. 
        # - DoesNotExist : if not matched with any objects 
        # - MultipleObjectReturned : if matched with more than one object 
        # student = Student.objects.get(pk=1)
        
        ##### FIRST : .first()
        # - returns the first object. if the queryset is not ordered, then it is ordfered by the primaty key, then returns the 1st object
        # - if the queryset is ordered by custom colums, then returns the 1st object based on that order 
        # - returns None if there is no object in the table 
        # student = Student.objects.first()
        # student = Student.objects.order_by('name').first()
        
        ##### LAST : .last()
        # same as first but the opposite, returns the last object based on the default or custom order 
        # # student = Student.objects.last()
        # student = Student.objects.order_by('name').last()
        
        ##### EARLIEST : .earliest(*fields) 
        # - it returns the earliest object based on that given fields. 
        # student = Student.objects.earliest('pass_date')
        
        ##### LATEST : .latest(*fileds)
        # - it returns the latest object based on that given field
        # student = Student.objects.latest('roll')
        
        ##### EXISTS : .exists()
        # - boolean. It returns true if the queryset has any object(s) else return false

        # checking if all the objects exist 
        # student = Student.objects.all()
        # print(Student.objects.all().exists())
        # print(student.exists())

        #  checking a single object if exist 
        # students = Student.objects.all()
        # one_data = Student.objects.get(pk=1)
        # student = students.filter(pk=one_data.pk).exists()
        # print(student)
        
        ##### CREATE : .create(**kwargs)
        # create() is a convenient method to create and save an object to a table 
        # Other way : obj = Student(name='ok', roll=110)
        #       - obj.save()
        # - .cretate way : obj = Student.objects.create(name='ok', roll=110) 
        #       - the object is created and saved in the model / database table 
        
        # student = Student.objects.create(name='Malim', class_name='X', roll=116, marks=65, pass_date='2023-8-25', city='Rng')  # date as : year-month-day
        
        ##### GET_OR_CREATE : .get_or_create(defaults=None, **kwargs)
        # it returns a touple. The object and a boolean created. It tries to get the object given in the kwargs. 
        # if the object is not found, then it crestes the object and returns it. 
        # along with the returned objects, it returns an boolena. if the object return if by get, then returns False, and the object 
        # was created, then returns True 
        # student, created = Student.objects.get_or_create(name='Salam', class_name='XI', roll=117, marks=75, pass_date='2023-8-25', city='Rng')
        # print(created)
        
        ##### UPDATE : .update(**kwargs) 
        # It performs SQL UPDATE query to update fields 
        # Remember - Update works in queryset, not in object. So getting the object using get and then update its fields won't work, we need to use filter 
        # Return - Update does not return any object, rather it returns an integer how many rows have been updated 
        # EX : 
        #       1. Update single objects fields : 
        # student = Student.objects.filter(pk=1).update(name='Updated Name Kalam', city='Updated Lalgola')

        # 2. Update multiple objects
        # student = Student.objects.filter(marks=90).update(city='Updated City Rng')
        
        # Error - The following way won't work as get returns an object, while update works on queryset 
        # student = Student.objects.get(pk=1).update(name='New Name')
        
        ##### UPDATE_OR_CREATE : .update_or_create(defaults=None, **kwargs)
        # It tries to update the object based on the kwargs, if the object is found then update it. If not found, then create the object. 
        # in the defaults, we have to pass the new data we want to the field as a dict {'field' : 'new value'} in this form. 
        # the kwargs is the values of which base the value will be searched and accessed. 
        # It returns a touple of object and a boolean whether the object was created (True) or updated (in this case, False as no object is created)
        
        # 18 pk was not available in the table, so this line will create the object, returns True as new object is created.  
        # student = Student.objects.update_or_create(pk=18, defaults={'name' : 'New Name Jahan', 'class_name':'XI', 'roll':118, 'marks':75, 'pass_date':'2023-8-25', 'city':'Rng'})

        # As the pk is already exist, this below code will only update the object and return false along with the object. 
        student, created = Student.objects.update_or_create(pk=18, defaults={'name' : 'Updated Name Jahan'})
        # print(created)
        
        ##### bulk_create and bulk_update 
        # These methos are convinient way to create or update objects in bulk order. 
        # see vid 87 (https://youtu.be/0eJeDxEb7Tw?t=2408) for more information 
        


        
        print("The Queryset : ",  student)

        return render(request, 'school/home.html', {'student' : student})