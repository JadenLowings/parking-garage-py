import os
import re
import time

from timeFunc import getTime

# Used to check operating system and
# clear the terminal with the correct command
def clear():
    from subprocess import call
    from platform import system

    opSys = system()
    if opSys == 'Windows':
        call('cls', shell = True)
    else:
        os.system('clear')

# Function reads given test file and inputs data
# into parkingLot.txt, fileName is given in main
def vehicleIn(fileName):

    parkingLot = open('parkingLot.txt', 'w') 
    file1 = open(fileName, 'r')

    count = 0
    parkingCount = 0

    clear()

    # Loops through each line in given file
    for line in file1: 
        count += 1

        # Sets the amount of parking bays avaliable
        if line.startswith('PB-'):
            line = re.sub('[PB-]', '', line)
            parkingBays = int(line.strip())
            print ('Avaliable bays: ', parkingBays)
            print('\n')
        
        # Scans the license plates and assigns parking bays in parkingLot.txt
        if line.startswith('LP-'):
            parkingCount += 1
            parkingBays -= 1

            print("Parking {}: {}".format(parkingCount, line.strip()))
            
            # Sleep() used to create a difference in time
            # time.sleep(2.5)

            systime = getTime()
            toWrite = ("Parking {}: {} Time In: {} ,".format(parkingCount, line.strip(), systime))
            parkingLot.writelines("%s\n" % toWrite)
            
            # When garage bays are full breaks back into main
            if parkingBays == 0:
                print('\n')
                print ('Garage is full...')
                break

    file1.close()
    parkingLot.close()