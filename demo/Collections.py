from collections import namedtuple
from collections import deque
from collections import Counter
from tkinter import E
a=namedtuple('A',['a','b'])
s=a(1,2)
print(s.a+s.b)


a=['a','e','i','o','u']

# d=deque(a)
# d.pop()
# print(d)
# count=Counter(a)
# print(count)


# try:
#     for i in range(5):
#         if i==1:
#             print(a[i]+2)
#         else:
#             print(a[i])
# except IndexError as e1:
#     print("Index is out of range")
# except TypeError as e2:
#     print("cannot add int and string")
# finally:
#     print("khatam")



class user_defined_exception(Exception):
    def __init__(self,message):
        self.message=message
        print(self.message)

try:
    if len(a)<5:
        raise user_defined_exception("length < 5") 
except user_defined_exception as e:
    print("error")


