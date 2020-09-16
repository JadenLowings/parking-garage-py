from random import randint

import re

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    
    return randint(range_start, range_end)

def getNumPlate():

    numList = []
    for _ in range(3):
        value = random_with_N_digits(2)

        numList.append(value)

    numList.append('GP')
    numberPlate = ' '.join([str(elem) for elem in numList])

    return numberPlate