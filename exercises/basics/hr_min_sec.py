# Write a getHoursMinutesSeconds() function that has a totalSeconds parameter. The
# argument for this parameter will be the number of seconds to be translated into the number of hours,
# minutes, and seconds. If the amount for the hours, minutes, or seconds is zero, don’t show it: the
# function should return '10m' rather than '0h 10m 0s'. The only exception is that
# getHoursMinutesSeconds(0) should return '0s'.

def getHoursMinutesSeconds(totalSeconds: int):
    
    if totalSeconds == 0:
        
        return '0s'
    
    elif totalSeconds < 3600:
        
        print(f"0h {int(totalSeconds/60)}m 0s")
        
    elif totalSeconds >= 3600:
        
        print(f"{int((totalSeconds/60)/60)}h 0m 0s")

getHoursMinutesSeconds(7800)