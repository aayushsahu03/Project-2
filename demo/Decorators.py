import math


def outer_function(func):
    def inner_function(*args,**kwargs):
        return func(*args,**kwargs)
    return inner_function

@outer_function
def myfunc(name,age):
    print(name,age)

myfunc("Aayush",27)

# TEMPLATE FOR WRAPPER AND DECORATED FUNCTION
# def decorator(func):
#     def wrapper():
#         return func()
#     return wrapper

# @decorator
# def func():
#   <do something>
#
# func()


class decorator_class(object):
    def __init__(self,original_func):
        self.func=original_func

    def __call__(self,*args,**kwargs): #behaves just like wrapper function
        print("call method executed this statement before {}".format(self.func.__name__))
        return self.func(*args,**kwargs)

@decorator_class
def myfunc2(name,age):
    print("I did this successfully")

myfunc2("Aayush",27)



#****************** using decorators in examples ************************

def my_logger(func):

    import logging
    logging.basicConfig(filename=f'{func.__name__}.log',level=logging.INFO)

    def wrapper(*args,**kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {} '.format(args,kwargs))
        return func(*args,**kwargs)
    return wrapper


def my_timer(func):
    import time
    def wrapper(*args,**kwargs):    
        t1=time.time()
        result=func()
        t2=time.time()
        return result
    return wrapper

@my_logger
def display_info(name,key,mode='web'):
    print(name,key,mode)

display_info("ajay","234fe1",mode='mobile')

print(print.__doc__)

        







