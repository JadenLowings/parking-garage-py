import random
import os
import re

from theBank import canPay
from vehicleIn import clear

# Function removes seperator and appends
# toReplace to the end of the string
def listReplace(str, toReplace, seperator):

    for i in str:
        result = str.split(seperator, 1)[0]
    
    result = result + toReplace
    return result

# Function opens parkingLot.txt, removes
# whitespaces and appends '\n' to each
# line of the file
def cleanUp():
    fileClean = open('parkingLot.txt', 'r')
    contentClean = fileClean.read()
    toClean = contentClean.split(',')

    for i in range(len(toClean)):
        if toClean[i].startswith('P'):
            toClean[i] = " ".join(toClean[i].split())
            toClean[i] = toClean[i] + ' ,' + '\n'

            fileWrite = open('parkingLot.txt', 'w')
            fileWrite.writelines(toClean)

    fileClean.close()
    fileWrite.close()

# Function checks whether a given line is
# occupied or not.
def isEmpty():
    fileCheck = open('parkingLot.txt', 'r')
    contentCheck = fileCheck.read()
    toCheck = contentCheck.split(',')

    parkingNum = len(toCheck)
    parkingNum = int(parkingNum) - 1
    clear()
    print('Parking Bays: 1 -', parkingNum)

    option = input()
    option = int(option) - 1

    for i in range(len(toCheck)):
        
        if option == -1:
            print ('Invalid Input')
            break
        elif option == parkingNum:
            print ('Invalid Input')
            break
        elif i == option:
            print(toCheck[i])

            input('Continue? ')
            clear()
    fileCheck.close()

# Function gets registration of vehicle
# before exit.
def getReg(str):
    seperator = "BA-"
    toReplace = ""
    
    strList = str.split('LP-')
    
    reg = strList[1]
    reg = listReplace(reg, toReplace, seperator)

    return reg

# Function creates a list of parkingLot.txt
# assigns a random number and then removes the
# corresponding vehicle
def vehicleOut():
    fileOpen = open('parkingLot.txt', 'r')

    content = fileOpen.read()
    parkingList = content.split('\n')
 
    listLen = len(parkingList)
    
    # To accomadate for the \n at the end of parkingLot.txt file
    result = listLen - 2
    
    # Randomly selecting a vehicle to exit the parking lot
    vehicleLeave = random.randint (0, result)

    lineList = parkingList
    PB = len(parkingList)
    PB = int(PB) - 1

    # For loop to iterate through the list
    # allowing line by line edits
    for i in range(len(parkingList)):
        if i == vehicleLeave:

            str_toReplace = ': Empty,'
            seperator = ':'
            
            isPayable = canPay(lineList[vehicleLeave])

            if isPayable == '404':
                clear()
                print ('Parking Bay Empty')
                print('\n')
                break
            
            reg = getReg(lineList[vehicleLeave])

            if isPayable == True:
                print('Vehicle:' + reg + 'left the garage.')
                print('\n')
                
                input('Continue?')
                lineList[vehicleLeave] = listReplace(lineList[vehicleLeave], str_toReplace, seperator)
                
                fileWrite = open('parkingLot.txt', 'w')
                fileWrite.writelines(lineList)
                
                fileWrite.close()
                fileOpen.close()
                
                cleanUp()


            else:
                print('Vehicle ' + reg + "Could not pay for parking and wasn't allowed to leave")
                break

            clear()