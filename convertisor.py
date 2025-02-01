def length():
    unit = {
        'km':{'hm':10, 'dam':100, 'm':1000, 'dm':10000, 'cm':100000, 'mm':1000000},
        'hm':{'km':0.1 ,'dam':10, 'm':100, 'dm':1000, 'cm':10000, 'mm':100000},
        'dam':{'km':0.01,'hm':0.1,'m':10, 'dm':100, 'cm':1000, 'mm':10000},
        'm':{'km':0.001,'hm':0.01,'dam':0.1,'dm':10, 'cm':100, 'mm':1000},
        'dm':{'km':0.0001,'hm':0.001,'dam':0.01,'m':0.1,'cm':10, 'mm':100},
        'cm':{'km':0.00001,'hm':0.0001,'dam':0.001,'m':0.01,'dm':0.1, 'mm':10},
        'mm':{'km': 0.000001, 'hm': 0.00001, 'dam': 0.0001, 'm': 0.001, 'dm': 0.01, 'cm': 0.1}
    }
    value = float(input("Please enter you value:"))
    old_unit = input("Please enter your actual unit:")
    new_unit = input("Please enter your new_unit:")
    return value * unit[old_unit][new_unit]

def liter():
    liter_unit = {
        'kl': {'hl': 10, 'dal': 100, 'l': 1000, 'dl': 10000, 'cl': 100000, 'ml': 1000000},
        'hl': {'kl': 0.1, 'dal': 10, 'l': 100, 'dl': 1000, 'cl': 10000, 'ml': 100000},
        'dal': {'kl': 0.01, 'hl': 0.1, 'l': 10, 'dl': 100, 'cl': 1000, 'ml': 10000},
        'l': {'kl': 0.001, 'hl': 0.01, 'dal': 0.1, 'dl': 10, 'cl': 100, 'ml': 1000},
        'dl': {'kl': 0.0001, 'hl': 0.001, 'dal': 0.01, 'l': 0.1, 'cl': 10, 'ml': 100},
        'cl': {'kl': 0.00001, 'hl': 0.0001, 'dal': 0.001, 'l': 0.01, 'dl': 0.1, 'ml': 10},
        'ml': {'kl': 0.000001, 'hl': 0.00001, 'dal': 0.0001, 'l': 0.001, 'dl': 0.01, 'cl': 0.1}
    }
    value = float(input("Please enter you value:"))
    old_unit = input("Please enter your actual unit:")
    new_unit = input("Please enter your new_unit:")
    return value * liter_unit[old_unit][new_unit]
def weight():
    weight_unit = {
        'kg': {'hg': 10, 'dag': 100, 'g': 1000, 'dg': 10000, 'cg': 100000, 'mg': 1000000},
        'hg': {'kg': 0.1, 'dag': 10, 'g': 100, 'dg': 1000, 'cg': 10000, 'mg': 100000},
        'dag': {'kg': 0.01, 'hg': 0.1, 'g': 10, 'dg': 100, 'cg': 1000, 'mg': 10000},
        'g': {'kg': 0.001, 'hg': 0.01, 'dag': 0.1, 'dg': 10, 'cg': 100, 'mg': 1000},
        'dg': {'kg': 0.0001, 'hg': 0.001, 'dag': 0.01, 'g': 0.1, 'cg': 10, 'mg': 100},
        'cg': {'kg': 0.00001, 'hg': 0.0001, 'dag': 0.001, 'g': 0.01, 'dg': 0.1, 'mg': 10},
        'mg': {'kg': 0.000001, 'hg': 0.00001, 'dag': 0.0001, 'g': 0.001, 'dg': 0.01, 'cg': 0.1}
    }


def temperature():
    temperature_unit={}