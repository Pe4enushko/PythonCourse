import functools


def get_factorial(num):
    u"""Docstring in unicode ыуыуыуыу"""
    
    print("Имя: " + get_factorial.__name__)
    print("Дока: " + str(get_factorial.__doc__))
    return functools.reduce(lambda a,b: a*b, range(1,num+1))

get_factorial(9)
