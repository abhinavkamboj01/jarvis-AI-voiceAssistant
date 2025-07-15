# # from playsound import playsound

import eel
import pygame
import pywhatkit as kit
import os
import re
import sys
import sqlite3
import subprocess  # subprocess is for macOS
import webbrowser
import time
import pvporcupine
import pyaudio
import struct
import pyautogui
from urllib.parse import quote
from hugchat import hugchat




# Add paths for module imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.helper import extract_yt_term, remove_words
from config import ASSISTANT_NAME  
from backend.command import speak  

# Initialize SQLite connection
conn = sqlite3.connect('jarvis.db')  
cursor = conn.cursor()  

# Initialize pygame mixer
pygame.mixer.init()

# Play assistant startup sound
@eel.expose
def play_assistant_sound():
    sound_file = os.path.join(os.getcwd(), "frontend/assets/audio/start_sound.mp3")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# Function to open applications or websites
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "").strip()  # Remove assistant name
    query = query.lower()
    query = query.replace("open", "").strip()  # Remove "open" and clean query
    
    if query != "":
        try:
            # 1️⃣ Check if it's a system application
            cursor.execute('SELECT path FROM sys_command WHERE name = ?', (query,))
            result = cursor.fetchone()

            if result:
                app_path = result[0]
                speak(f"Opening {query}")
                subprocess.run(["open", "-a", app_path])  # ✅ Works on macOS

            else:
                # 2️⃣ Check if it's a web application
                cursor.execute('SELECT url FROM web_command WHERE name = ?', (query,))
                result = cursor.fetchone()

                if result:
                    url = result[0] 
                    speak(f"Opening {query}")
                    webbrowser.open(url)  # ✅ Opens websites in the browser

                else:
                    # 3️⃣ Try opening it as a general app (fallback)
                    speak(f"Trying to open {query}")
                    
                    try:
                        subprocess.run(["open", "-a", query])  # ✅ Works on macOS
                    except:
                        speak(f"Could not find {query}")

        except Exception as e:
            speak("Something went wrong")
            print(f"Error: {e}")



# Function to play YouTube videos
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak(f"Playing {search_term} on YouTube")
        kit.playonyt(search_term)




def findContact(query):

    words_to_remove = [ASSISTANT_NAME, "make", "a", "to", "phone", "call", "send", "message", "whatsapp", "video"]
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT phone FROM contacts WHERE LOWER(name) LIKE ?", (f"%{query}%",))
        results = cursor.fetchall() # fetching all the results of that name
        print(results[0][0])
        mobile_number_str = str(results[0][0]) # converting the number into string

        if not mobile_number_str.startswith("+91"):
            mobile_number_str = "+91" + mobile_number_str

        return mobile_number_str, query
    except:
        speak("Not exist in contacts")
        return 0, 0
    

# for performing operation using whatsapp

def whatsApp(phone, message, flag, name):

    if flag == "message":
        jarvis_message = f"Message sent successfully to {name}"
        whatsapp_url = f"whatsapp://send?phone={phone}&text={quote(message)}"

    else:
        jarvis_message = f"{'Calling' if flag == 'call' else 'Starting video call with'} {name}"
        whatsapp_url = f"whatsapp://send?phone={phone}"

    # Open WhatsApp contact
    full_command = f'open -a "WhatsApp" "{whatsapp_url}"'
    subprocess.run(full_command, shell=True)
    time.sleep(5)  # Wait for WhatsApp to fully load

    # Automate the call or video call
    if flag != "message":
        # Adjust this depending on screen resolution or element position
        pyautogui.hotkey("cmd", "f")  # Focus on search bar (if needed)
        time.sleep(2)
        
        # Simulate tabbing to the call buttons
        if flag == "call":
            # Simulate clicking the phone icon (adjust coordinates if needed)
            pyautogui.hotkey("tab", interval=0.5)  # Tab to call button
            pyautogui.press("enter")
        else:
            # Simulate clicking the video call icon
            pyautogui.hotkey("tab", interval=0.5)  # Tab to video call button
            pyautogui.hotkey("tab", interval=0.5)
            pyautogui.press("enter")

    speak(jarvis_message)


def chatBot(query):
    user_input = query.lower()
    
    chatBot = hugchat.ChatBot(cookie_path = "backend/cookie.json")
    id = chatBot.new_conversation()
    chatBot.change_conversation(id)
    response = chatBot.chat(user_input)
    print(response)
    speak(response)
    return response

