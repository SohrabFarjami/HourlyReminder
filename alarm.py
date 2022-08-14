from datetime import datetime
from text_to_speech import speak
from time import time, sleep
import os
from gtts import gTTS
import vlc

stop = False ## To loop forever
while stop == False:
    now = datetime.now()
    second = now.second
    minute = now.minute
    if second == 0 and minute == 0:
        myText = 'It is now ' + (now.strftime("%I %p"))
        print(myText)
        output = gTTS(text=myText, lang='en', slow=False)
        output.save("Time.mp3")
        p = vlc.MediaPlayer("Time.mp3")
        p.play()
        sleep(10)
        os.remove("Time.mp3")


        
        
        


