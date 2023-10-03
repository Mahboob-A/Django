from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView
# Create your views here.

class StudentListView(ListView): 
        model = Student
        template_name = 'school/show_data.html'
        context_object_name = 'st_data'  # here object_name context name will also work alongside custom context naem 
        ordering = ['-name']
        
        ''' 
        the above code in enough to display all model data. The below code is used to manipulate the data to show
        to show just all the data, the above code is enough 
        '''
        def get_queryset(self): 
                return Student.objects.filter(course='Django')   # this will apply in the default or custom context variable 
        
        # here creating a new context. we can create any extra context using get_context_data method. 
        def get_context_data(self, *args, **kwargs): 
                context = super().get_context_data(*args, **kwargs)
                context['ordered_courses'] = Student.objects.all().order_by('course')
                context['greetings'] = 'Good Morning Today is 090723, Sunday, 09.00 am'
                return context 
        
       
        def get_template_names(self) -> list[str]:
                ''' Using get_template_names method, we can specify which template to render in specific cases. '''
                if self.request.user.is_superuser:
                        template_name = 'school/superuser.html'
                elif self.request.user.is_staff: 
                        template_name = 'school/staff.html'
                else: 
                        template_name = self.template_name 
                return [template_name]
                

'''
class StudentListView(ListView): 
        model = Student
        
        
        In this view also, the same thing will work but here we have to work with 
        default variable names. 
        The default context name will be : ModelName_list 
        and the contenxt variable name will be : ModelName_list and object_list  (we can use both context name)
        
        we have use the default variable names in this case. 
        
        If we use: 
                template_name_suffix = '_info'
                then all the default _list name will be changed to _info i.e ModelName_info
                

'''