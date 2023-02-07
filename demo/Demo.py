

from datetime import datetime
from traceback import print_tb


class employee:
    num_emps=0
    raise_amt=1.04

    def __init__(self,first=None,last=None,salary=0):
        self.first_name=first
        self.last_name=last
        self.salary=salary

        employee.num_emps+=1

    def print_details(self):
        print(f'{self.first_name} {self.last_name}\n {self.salary}')

    def apply_raise(self):
        self.salary*=self.raise_amt
    
    @classmethod
    def set_raise_amt(cls,amount): # passing class
        '''
            param: cls,amount
        '''
        cls.raise_amt=amount
    @staticmethod
    def is_workday(day):  # static method independent of class and instance
        if (day.weekday()==5 or day.weekday()== 6):
            return False
        return True

emp1=employee("Aayush","Sahu",65000)
emp1.print_details()
employee.set_raise_amt(1.05)
emp1.apply_raise()
emp1.print_details()
print(emp1.is_workday(datetime.today())) # if today is workday or not
print(datetime.weekday(datetime.today())) # Mon:0 Sun:6



class programmer(employee):
    raise_amt=1.1

    def __init__(self, first, last, salary,prog_lang):
        super().__init__(first, last, salary)
        self.lang=prog_lang
    


emp2=employee(salary=60000)
emp2.apply_raise()
emp2.print_details()

emp3=programmer("peyush","bansal",salary=60000,prog_lang="java")
emp3.apply_raise()
emp3.print_details()
print("*"*50,"\n\n\n")
#****************** special methods *****************************
print(emp3.__sizeof__())

