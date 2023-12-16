
# built in auth signals
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.db.models.signals import pre_init, pre_save, pre_delete,  pre_migrate,  post_init, post_save, post_delete, post_migrate
from django.contrib.auth.models import User
from django.dispatch import receiver 

@receiver(user_logged_in, sender=User)
def user_login_receiver(sender, request, user, **kwargs): 
        print('################## login signal receiver ####################')
        print('sender: ', sender)
        print('request: ', request)
        print('user: ', user)
        print(f'kwargs: {kwargs}')
        
# manual connect 
# user_logged_in.connect(user_login_receiver, sender=User)

# @receiver(user_logged_out, sender=User)
def user_logout_receiver(sender, request, user, **kwargs): 
        print('################## logout signal reciever ####################')
        print('sender: ', sender)
        print('request: ', request)
        print('user: ', user)
        print(f'kwargs: {kwargs}')
        
# manual connect 
user_logged_out.connect(user_logout_receiver, sender=User)
        
        
@receiver(user_login_failed)
def user_login_failed_receiver(sender, credentials, request, **kwargs): 
        print('################## login failed signal reciever ####################')
        print('sender: ', sender)
        print('request: ', request)
        print('credentials: ', credentials)
        print(f'kwargs: {kwargs}')
          
        
# manual connect 
# user_login_failed.connect(user_login_failed_receiver)


''' Model Signals '''

@receiver(pre_save, sender=User)
def pre_save_receiver(sender, instance, **kwargs): # we can also take all the params in kwargs for db signals 
        print('############### Pre_Save Receiver ###############')
        print('sender: ', sender)
        print('instance: ', instance)
        print(f'kwargs: , {kwargs}')

# pre_save.connect(pre_save_receiver, sender=User)

@receiver(post_save, sender=User)
def post_save_receiver(sender, instance, created, **kwargs): # we can also take all the params in kwargs for db signals 
        print('############### Post_Save Receiver ###############')
        print('sender: ', sender)
        print('instance: ', instance)
        print('created: ', created)
        print(f'kwargs: , {kwargs}')

# post_save.connect(post_save_receiver, sender=User)







