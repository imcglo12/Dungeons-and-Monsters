#This program will create random numbers for all of the different
#     types of dice

#import necessary libraries
from random import randint

#defining the functions
def d4():
    d4 = randint(1, 4)
    return d4

def d6():
    d6 = randint(1, 6)
    return d6

def d8():
    d8 = randint(1, 8)
    return d8

def d12():
    d12 = randint(1, 12)
    return d12

def d10():
    d10 = randint(1, 10)
    return d10

def d10p():
    rand_num = randint(0, 9)
    d10p = rand_num*10
    if d10p == 0:
        d10p = 100
    return int(d10p)

def d20():
    d20 = randint(1, 20)
    return d20
