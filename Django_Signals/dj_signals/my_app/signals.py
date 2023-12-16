
# built in auth signals
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.db.models.signals import pre_init, pre_save, pre_delete,  pre_migrate,  post_init, post_save, post_delete, post_migrate
from django.contrib.auth.models import User
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












