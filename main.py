import os
import eel
from backend.feature import *
from backend.command import *
from backend.auth import recognize
from backend.auth.recognize import AuthenticateFace

eel.init("frontend")

play_assistant_sound()
@eel.expose
def init():
    eel.hideLoader()
    speak("Welcome to Jarvis")
    speak("Ready for Face Authentication")
    flag = recognize.AuthenticateFace()
    if flag == 1:
        speak("Face recognized successfully")
        eel.hideFaceAuth()
        eel.hideFaceAuthSuccess()
        speak("Welcome to Jarvis")
        eel.hideStart()
        play_assistant_sound()
    else:
        speak("Face not recognized, please try again")


os.system('open -a "Google Chrome" --args --app= http://127.0.0.1:5500/frontend/index.html')  # it will open in this port 

eel.start('index.html', size=(1000, 600))



