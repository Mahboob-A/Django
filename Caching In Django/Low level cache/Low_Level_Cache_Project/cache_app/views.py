from django.shortcuts import render

from django.core.cache import cache 

def home(request): 
        cached_value = ''
        ''' cache get and set  ''' 
        cached_value = cache.get('name', None)
        if not cached_value: 
                cache.set('name', 'Mahboob Alam', 50, version=1)
        
        ''' cache get or set '''
        # cached_value = cache.get_or_set('name', 'Mahboob Alam', 20)
        
        ''' cache add  '''
        # cached_value = cache.add('name', 'Mehboob', 20)
        # print(cached_value)
        # cached_value = cache.get('name', 'Expired')
        
        st_info = {'name' : 'Mehboob', 'roll' : 101, 'stream' : 'CSE', 'subjects' : {'core' : ['Discreet Math, DAA, OS, CN'], 'support_subjects' : ['English', 'Communications']}}
        
        ''' cache set many and get many '''
        
        # cached_value = cache.get_many(st_info, version=1)
        
        # if not cached_value:
        #         cache.set_many(st_info, 300, version=1)
        
        ''' cache delete and cache delete many  '''
        # cache.delete('name')
        # cache.delete_many(st_info)
        # cached_value = cache.get('stream', 'deleted')
        
        '''  cache incr and decr works to increase and decrease a cached value '''
        # cache.set('val', 10, 120)
        # cache.incr('val', delta=1)
        # cached_value = cache.get('val', 'error happened')
        
        ''' cache clear - deletes all the cache from backend '''
        # cache.clear()
        
        return render(request, 'cache_app/home.html', {'cached_value' : cached_value})

def home2(request): 
        return render(request, 'cache_app/home2.html')

