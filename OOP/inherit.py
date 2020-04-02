#Inheritance 
class Employee:
    
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    pass

dev1 = Developer('Tony','Jack', 10000)
dev2 = Developer('Mery','Fu',50000)
print(dev1.email)
print(dev2.email)