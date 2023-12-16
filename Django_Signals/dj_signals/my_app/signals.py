
# built in auth signals
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

# built in db signals 
from django.db.models.signals import pre_init, pre_save, pre_delete,  post_init, post_save, post_delete

# built in request response signals 
from django.core.signals import request_started, request_finished, got_request_exception

# management work / django admin / model migration related signals 
from django.db.models.signals import pre_migrate, post_migrate 

from django.contrib.auth.models import User

# receiver decorator 
from django.dispatch import receiver

# we can take all the params in kwargs 

@receiver(user_logged_in, sender=User)
def user_login_receiver(sender, request, user, **kwargs): 
        print()
        print('################## login signal receiver ####################')
        print('sender: ', sender)
        print('request: ', request)
        print('user: ', user)
        print(f'kwargs: {kwargs}')
        print()
        
# manual connect 
# user_logged_in.connect(user_login_receiver, sender=User)

# @receiver(user_logged_out, sender=User)
def user_logout_receiver(sender, request, user, **kwargs): 
        print()
        print('################## logout signal reciever ####################')
        print('sender: ', sender)
        print('request: ', request)
        print('user: ', user)
        print(f'kwargs: {kwargs}')
        print()
        
# manual connect 
user_logged_out.connect(user_logout_receiver, sender=User)
        
        
@receiver(user_login_failed)
def user_login_failed_receiver(sender, credentials, request, **kwargs): 
        print()
        print('################## login failed signal reciever ####################')
        print('sender: ', sender)
        print('request: ', request)
        print('credentials: ', credentials)
        print(f'kwargs: {kwargs}')
        print()
          
        
# manual connect 
# user_login_failed.connect(user_login_failed_receiver)


''' Model Signals '''

''' 
pre save and post save 
pre_save is sent  before model save() method 
and post_save is sent just after model save() mehtod 
'''
@receiver(pre_save, sender=User)
def pre_save_receiver(sender, instance, **kwargs): 
        print()
        print('############### Pre_Save Receiver ###############')
        print('sender: ', sender)
        print('instance: ', instance)
        print(f'kwargs: , {kwargs}')
        print()

# pre_save.connect(pre_save_receiver, sender=User)

@receiver(post_save, sender=User)
def post_save_receiver(sender, instance, created, **kwargs): 
        print()
        print('############### Post_Save Receiver ###############')
        print('sender: ', sender)
        print('instance: ', instance)
        print('created: ', created)
        print(f'kwargs: , {kwargs}')
        print()

# post_save.connect(post_save_receiver, sender=User)




'''
pre and post delete 
pre_delete is sent just before model's delete() method 
and post_delete is sent just after model's delete() method
'''


@receiver(pre_delete, sender=User)
def pre_delete_receiver(sender, instance, **kwargs): 
        print()
        print('############### Pre_Delete Receiver ###############')
        print('sender: ', sender)
        print('instance: ', instance)
        print('instance property username: ', instance.username)
        print('instance property password: ', instance.password)
        print('instance property first_name: ', instance.first_name)
        print('instance property last_name: ', instance.last_name)
        print('instance property email: ', instance.email)
        print(f'kwargs: , {kwargs}')        
        print()
        
# pre_delete.connect(pre_delete_receiver, sender=User)

@receiver(post_delete, sender=User)
def post_delete_receiver(sender, instance, **kwargs): 
        print()
        print('############### Post_Delete Receiver ###############')
        print('sender: ', sender)
        print('instance: ', instance)
        print('instance property username: ', instance.username)
        print('instance property password: ', instance.password)
        print('instance property first_name: ', instance.first_name)
        print('instance property last_name: ', instance.last_name)
        print('instance property email: ', instance.email)
        print(f'kwargs: , {kwargs}')        
        print()

# post_delete.connect(post_delete_receiver, sender=User)


'''
pre and post init 
init signals are sent when we instantiate a django model 

pre_init is sent just before the __init__() is called when we instantiate a django model 
post_init is sent just after the __init__() is finished, i.e. when the django model instance has been created
'''



@receiver(pre_init, sender=User)
def pre_init_receiver(sender, *args, **kwargs): 
        print()
        print('############### Pre_INIT Receiver ###############')
        print('sender: ', sender)
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        print()
        

# pre_init.connect(pre_init_receiver, sender=User)


@receiver(post_init, sender=User)
def post_init_receiver(sender, *args, **kwargs): 
        print()
        print('############### Post_INIT Receiver ###############')
        print('sender: ', sender)
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        print()
        
# post_init.connect(post_init_receiver, sender=User)


'''
request_started, request_finished, got_request_exception

request_started : when a http request beings to process 

request_finished : when a http request has been successfully processed 

got_request_exception : when an exception is occured processing a http request   

'''

@receiver(request_started)
def request_started_receiver(sender, environ, **kwargs): # environ 
        print()
        print('############### HTTP Request Started Receiver ###############')
        print('sender: ', sender)
        print('environ: ', environ)
        print(f'kwargs: {kwargs}')
        print()

# request_started.connect(request_started_receiver)

@receiver(request_finished)
def request_finished_receiver(sender, **kwargs): 
        print()
        print('############### HTTP Request Finished Receiver ###############')
        print('sender: ', sender)
        print(f'kwargs: {kwargs}')
        print()


# request_finished.connect(request_finished)


@receiver(got_request_exception)
def got_request_exception_receiver(sender, request, **kwargs): 
        print()
        print('############### HTTP Request Got Exception Receiver ###############')
        print('sender: ', sender)
        print('request: ', request)
        print(f'kwargs: {kwargs}')
        print()

# got_request_exception.connect(got_request_exception)




'''
pre and post migrate 

pre_migrate - this signal is sent just before the migration begins 

post_migrate - this signal is sent just after the migration ends and flush command run.    

NB : For each app, these signals will run 

'''


@receiver(pre_migrate)
def pre_migrate_receiver(sender, **kwargs): 
        print()
        print('############### Pre_Migrate Receiver ###############')
        print('sender: ', sender)
        print(f'kwargs: {kwargs}')        
        print()
        
# pre_migrate.connect(pre_migrate_receiver)


@receiver(post_migrate)
def post_migrate_receiver(sender, **kwargs): 
        print()
        print('############### Post_Migrate Receiver ###############')
        print('sender: ', sender)
        print(f'kwargs: {kwargs}')        
        print()

# post_migrate.connect(post_migrate_receiver)



