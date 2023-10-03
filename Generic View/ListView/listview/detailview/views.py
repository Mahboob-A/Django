from django.shortcuts import render

# Create your views here.
from .models import Teacher
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


'''
DetailView works on a single database object. It takes a primary key and returns the database object of that 
pk 
'''


class TeacherDetailView(DetailView): 
        ''' a detailview to show uniquie teacher details '''
        model = Teacher
        # template_name = 'detailview/teacher.html'  # default is teacher_detail.html 
        # context_object_name = 'teacher_data'   # default is ModelName i.e 'teacher '
        # pk_url_kwarg = 'search_id' # default is pk (we need to put this in the urls )
        
        # this shows all the teache names while shoing one teacher details 
        def get_context_data(self, *args, **kwargs): 
                context = super().get_context_data(*args, **kwargs)
                context['all_teacher_data'] = Teacher.objects.all()
                return context
        


class SubjectTeacherListView(ListView): 
        ''' this view shows all the teachers associated to a particular subject '''
        model = Teacher
        template_name = 'detailview/show_subject_based_teachers.html'
        context_object_name = 'subject_data'
        pk_url_kwarg = 'sub'


        # this method purely works on the geeting data form the model 
        def get_queryset(self): 
                # print(self.kwargs)
                subject = self.kwargs['sub']   # sub is getting from the url. here the subject is taken and returning all the teachers based on the subject 
                return Teacher.objects.filter(subject=subject)

        # to show the subject name in the frontend 
        def get_context_data(self, *args, **kwargs): 
                context = super().get_context_data(*args, **kwargs)
                subject = self.kwargs['sub']
                # print(subject)
                context['sub'] = subject
                return context


 
                
        
        

# main List view (shows all teachers and all subjects)
class GeneralListView(ListView): 
        model = Teacher
        template_name = 'detailview/show_data.html' # DEFAULT : teacher_list.html 
        context_object_name = 'subject_data' # DEFAULT : teacher_list and object_list (object_list can be used any time)        

        # showing only the unique subjects
        def get_queryset(self):  
                return Teacher.objects.values('subject').distinct()  # only getting the unique data of subject 
        
        # showing all the subjects 
        def get_context_data(self, *args, **kwargs): 
                context = super().get_context_data(*args, **kwargs)
                context['all_teachers'] = Teacher.objects.all()
                return context 
        

