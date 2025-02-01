def length():
    unit = {
        'km':{'hm':10, 'dam':100, 'm':1000, 'dm':10000, 'cm':100000, 'mm':1000000},
        'hm':{'km':0.1 ,'dam':10, 'm':100, 'dm':1000, 'cm':10000, 'mm':100000},
        'dam':{'km':0.01,'hm':0.1,'m':10, 'dm':100, 'cm':1000, 'mm':10000},
        'm':{'km':0.001,'hm':0.01,'dam':0.1,'dm':10, 'cm':100, 'mm':1000},
        'dm':{'km':0.0001,'hm':0.001,'dam':0.01,'m':0.1,'cm':10, 'mm':100},
        'cm':{'km':0.00001,'hm':0.0001,'dam':0.001,'m':0.01,'dm':0.1, 'mm':10}
    }
    value = float(input("Please enter you value:"))
    old_unit = input("Please enter your actual unit:")
    new_unit = input("Please enter your new_unit:")
    return value * unit[old_unit][new_unit]

def liter():
    unit = {
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
    return value * unit[old_unit][new_unit]

