import datetime
from text_to_speech import speak
from time import time, sleep
    
print('Time management protocol activated')
stop = False ## To loop forever
while stop == False:
    now = datetime.datetime.now()
    sleep(1 - time() % 1)
    print(now.second)
    if now.minute == 00 and now.second == 0: ##When minute and second is both 0 is it new hour
        armyHour = now.hour
        if armyHour == 12:
            messageUser = ('It is now 12 pm')
        elif armyHour == 24:
            messsageUser = ('It is now 12 am')
        elif armyHour > 12:
            standardHour = armyHour - 12 
            messageUser = ('It is now ' + str(standardHour) + 'pm')
        else:
            messageUser = ('It is now ' + str(armyHour) + 'am')
        
        speak(messageUser, "en", save=True, file="schedule.mp3")
        
        


