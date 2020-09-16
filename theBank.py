import time
import re
import math

from datetime import datetime
from timeFunc import getTime

# This function takes two strings and changes
# them into datetime objects in order to calculate
# the difference between the two dates and multiply
# the difference by the cost p.min function then
# returns the total cost of the parking
def payTotal(timeIn, payMin):
    # Used float to retain the decimal when getting totalCost
    cost = float(payMin)
    # Str to Obj
    timeIn = datetime.strptime(timeIn, '%d-%m-%Y %H;%M;%S')
    timeExit = getTime()
    # Str to Obj
    timeExit = datetime.strptime(timeExit, '%d-%m-%Y %H;%M;%S')
    print ('Time of exit: ', timeExit)

    timeTotal = timeIn - timeExit
    timeSeconds = timeTotal.total_seconds()
    
    timeMinutes = timeSeconds/60
    # Making the value a positive number
    timeMinutes = timeMinutes * -1

    timeMinutes = math.trunc(timeMinutes)
    
    totalCost = 0
    # Float used to keep the .5 of cost
    totalCost = float(totalCost)
    totalCost = (timeMinutes * cost)

    print ('Total Minutes: ', timeMinutes)
    print('Price: R', float(totalCost))
    print('\n')

    return totalCost

# Compares the amount due to the amount the vehicle has.
def canPay(str, timeIn, payMin):
    amountHave = int(str)
    amountDue = payTotal(timeIn, payMin)
    # Returns Boolean True = can leave
    #                False = can't leave
    
    # If parking is free < 1 min vehicles can leave.
    if amountDue == 0:
        return (True, 0)
    # If vehicles have enough money they may leave.
    elif amountHave > amountDue:
        return (True, amountDue)
    else:
        return (False, amountDue)