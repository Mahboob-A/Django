
# built in auth signals
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
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