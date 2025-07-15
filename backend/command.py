import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
    text = str(text)
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
   
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Karen') # Karen

    voices = engine.say(text)
    engine.runAndWait()
    eel.receiverText(text)

# speak("Hello, I am Jarvis. How can I help you today?")


@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening...")
        eel.DisplayMessage("I am Listening...") # Display message in the browser
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 8) # the mic will be on for 10 seconds and the audio will be recorded for 8 seconds

    # try to convert the audio to text
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")       # Display message in the browser
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
        eel.DisplayMessage(query)                  # Display query in the browser
        eel.senderText(query)
        speak(query)
        
    except Exception as e:
        print(f"Error: {str(e)}/n")
        return None
        
    return query.lower()
    
# text1 = takecommand()
# speak(text1)

@eel.expose
def takeAllCommands(message = None):
    print("Taking all commands...", message)
    try:
        query = takecommand()
        print(query)
        # eel.senderText(query)
        if "open" in query:
            import pdb; pdb.set_trace() 
            from backend.feature import openCommand
            openCommand(query)
            speak(f"Opening {query}")
            
        elif "on youtube" in query:                       # for using youtube
            from backend.feature import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "call" in query or "video call" in query:
            print("hellooo")
            from backend.feature import findContact, whatsApp
            flag = ""
            phone,name = findContact(query)
            if (phone) != 0:
                
                if "send message" in query:
                    flag = "message"
                    speak("What message to send")
                    query = takecommand()
                elif "call" in query:
                    flag = "call"
                else:
                    flag = "video call"
                        
                whatsApp(phone, query, flag, name)
        
        else:
            import traceback

            try:
                from backend.feature import chatBot
                chatBot(query)
            except Exception as e:
                print("An error occurred:", e)
                print(traceback.format_exc())

    except Exception as e:
        print("An error occurred while taking commands:", e)
        print("An error occured",e)

    eel.ShowHood()