from math import pow
from random import gauss
from math import trunc

def bet_zero_hun(inte):

    return min(100,max(inte,0))

def perish_func(amount,days):

    return pow(amount,1.0 - pow(days,-1.5))

def cut_off_gauss(a,b,mu,sigma):

    return min(b,max(a,gauss(mu,sigma)))

def trunc2(x):

    return 0.01 * trunc(100 * x)

def updown(num):

    if num >= 0:
        
        return "Up"

    else:
        
        return "Down"

def isripe(boolean):

    if boolean:

        return "Check"

    else:

        return "Empty"
