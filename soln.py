import math 
from pprint import pprint

def passwordStrength(password):
    
    unique_chars = ""
    for c in password:
        if c not in unique_chars:
            unique_chars += c
    
    char_groups = {
        'lc':{
            'group_size' : 0,
            'growth_fact': 0.25,
            'rep_fact' : 0,
            'max_group_size' : 26
        },
        'uc': {
            'group_size' : 0,
            'growth_fact': 0.4,
            'rep_fact' : 0,
            'max_group_size' : 26
        },
        'di': {
            'group_size' : 0,
            'growth_fact': 0.4,
            'rep_fact' : 0,
            'max_group_size' : 10
        },
        'sp': {
            'group_size' : 0,
            'growth_fact': 0.5,
            'rep_fact' : 0,
            'max_group_size' : 32
        }
    }
    
    #Find number of unique characters and group them
    for c in list(unique_chars):
        if c.isalpha():
            if c.islower():
                char_groups['lc']['group_size'] += 1
            else:
                char_groups['uc']['group_size'] += 1
        elif c.isdigit():
            char_groups['di']['group_size'] += 1
        else:
            char_groups['sp']['group_size'] += 1
    
    
    # exit()
    
    #Repition factor
    for char_group in char_groups:
        char_groups[char_group]['rep_fact'] = 1 - pow((1 - char_groups[char_group]['growth_fact']), char_groups[char_group]['group_size'])
    
    #Digit Strength
    digStrength = 0
    for char_group in char_groups:
        digStrength += char_groups[char_group]['rep_fact']*char_groups[char_group]['max_group_size']
    digStrength = pow(digStrength, len(password))
    
    #Password Strength
    passwordStrength = math.log(digStrength, 2)
    
    return passwordStrength

