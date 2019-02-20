import functools
from functools import partial
import django


def sum(*args):
    re = 0
    for arg in args:
        re +=arg
    return re

sum_base30 = partial(sum, 10, 20)
re = sum_base30(1 , 2)
print(sum.__name__)
print(sum_base30)


age = 19

def addage():
    global  age
    age = age + 1

addage()
print(age)







'''
def my_dec(*args, **kwargs):

    def decoretor(func):
        @functools.wraps(func)
        def my_run():
            print("prepare~~~~~~~~~~~~~~")
            f =func
            re = func()
            print("end~~~~~~~~~~")
            return re

        return my_run

    return decoretor

@my_dec()
def run():
    print("run!!!!!!!!!!!!!!")
    return str


f = run()
print("*"*20)
print(run)
print(f)
print(f.__name__)
print(run.__name__)
f()
'''