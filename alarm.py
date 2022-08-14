from datetime import datetime
from text_to_speech import speak
from time import time, sleep
    
print('Time management protocol activated')
stop = False ## To loop forever
while stop == False:
    now = datetime.now()
    if now.minute == 0 and now.second == 0: ##When minute and second is both 0 its a new hour     
        messageUser = ('It is now ' + now.strftime("%I %p"))
        speak(messageUser, "en", save=True, file="schedule.mp3")
        
        


