from math import pow

def bet_zero_hun(inte):

    return min(100,max(inte,0))

def perish_func(amount,days):

    return pow(amount,1.0 - pow(days,-1.5))
