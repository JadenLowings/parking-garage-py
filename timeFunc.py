from datetime import datetime

# Function retrieves the current date/time
# used when entering and leaving the parking.

def getTime():
    time = datetime.now()
    timeStr = time.strftime('%d-%m-%Y %H;%M;%S')

    return timeStr