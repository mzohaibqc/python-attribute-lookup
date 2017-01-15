
# coding: utf-8

# In[1]:

class A(object):
    pass

obj = A()
obj.a


# In[2]:

class A(object):
    def __getattr__(self, name):
        print('Getting an non-existing property on object: {}'.format(name))
        return 'Some default value'

obj = A()
obj.a


# In[3]:

class A(object):
    a = 123

obj = A()
obj.a


# In[4]:

# First we need to define a descriptor class
class Desc(object):
    def __get__(self, instance, klass):
        print('Getting value from non-data descriptor')
        return 'default value defined by __get__'

class A(object):
    a = Desc()

obj = A()
obj.a


# In[6]:

class A(object):
    def __init__(self):
        self.a = 123

obj = A()
obj.a


# In[20]:

class Desc(object):
    
    def __init__(self, val=None):
        self.val = val
        
    def __get__(self, instance, klass):
        print('Getting value from non-data descriptor')
        return self.val
    
    def __set__(self, instance, val):
        print('data descriptor __set__')
        self.val = val

class A(object):
    a = Desc(111)

obj = A()
print('a' in A.__dict__)
print(hasattr(A.__dict__['a'], '__get__') and hasattr(A.__dict__['a'], '__set__'))
# obj.__dict__['a'] = 123
obj.a


# In[22]:

class B():
    pass

B.b


# In[24]:

class Meta(type):
    def __getattr__(cls, name):
        print('Getting an non-existing property on Class: {}'.format(name))
        return 'Some default value'

class B():
    __metaclass__ = Meta

B.b


# In[26]:

class Meta(type):
    b = 123

class B(object):
    __metaclass__ = Meta

B.b


# In[48]:

class ClassDesc(object):
    def __get__(self, cls, meta):
        print('Getting value from non-data descriptor')
        return 'default value defined by __get__'

class Meta(type):
    b = ClassDesc()
    
class B(object):
    __metaclass__ = Meta
    
B.b


# In[28]:

class B(object):
    b = 123
    
B.b


# In[39]:

class Meta(type):
    def __new__(cls, name, bases, cdict):
        cdict['b'] = 1234
        return type.__new__(cls, name, bases, cdict)

class B(object):
    __metaclass__ = Meta
    
B.b


# In[50]:

class ClassDesc(object):
    
    def __init__(self, val=None):
        self.val = val
        
    def __get__(self, cls, meta):
        print('Getting value from non-data descriptor')
        return self.val
    
    def __set__(self, cls, val):
        print('data descriptor __set__')
        self.val = val

class Meta(type):
    
    b = ClassDesc(1111)
    
    def __new__(cls, name, bases, cdict):
        cdict['b'] = 1234
        return type.__new__(cls, name, bases, cdict)
    
class B(object):
    __metaclass__ = Meta

print('b' in Meta.__dict__)
print(hasattr(Meta.__dict__['b'], '__get__') and hasattr(Meta.__dict__['b'], '__set__'))
B.b


# In[51]:

B.b = 1


# In[ ]:




# In[ ]:



