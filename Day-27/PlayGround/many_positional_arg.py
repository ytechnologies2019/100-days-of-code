from numpy.ma.core import multiply


def numbers(*args):
    print (args[3])
    sum = 0
    for n in args:
        sum += n
    return sum

print (numbers(3, 5, 7 , 10))

def calculate(n , **kwargs):
    print(kwargs) ## Dictionary Type
    for (key, value) in kwargs.items():
        print (key)
        print (value)
    n  *= kwargs['multiply']
    n  += kwargs['add']

    print(n)

calculate(2, add=3 , multiply=5)

class Car:
    def __init__(self , **kw):
        self.make = kw.get('make')    ##If key does not exist in kw , return none
        self.model = kw.get('model')
        self.colour = kw.get('blue')
        self.seat   = kw.get(4)

mycar = Car(make="Toyota" , model='2019')
print (mycar.make)
print (mycar.model)

