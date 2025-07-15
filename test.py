# # # import pvporcupine
# # # import struct
# # # import time
# # # import pyaudio

# def hotword():
#     porcupine = None
#     paud = None
#     audio_stream = None  # for streaming audio in background with microphone
#     try:

#         # pre trained keywords
#         porcupine = pvporcupine.create(keywords=["jarvis","alexa"]) # these two are already trained
#         paud = pyaudio.PyAudio()
#         audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
#         # loop for streaming
#         while True:
#             # to keep microphone always on
#             keyword=audio_stream.read(porcupine.frame_length)
#             keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

#             # processing keyword comes from mic 
#             keyword_index=porcupine.process(keyword) # checking the keyword (either it is  jarvis or alexa)

#             # checking first keyword detected or not
#             if keyword_index>=0:
#                 print("hotword detected")

#                 # pressing shorcut key ctrl+j( jb hotword keyword milega to apne aap hi ye keys press ho jayenge)
#                 import pyautogui as autogui
#                 autogui.keyDown("ctrl")
#                 autogui.press("j")
#                 time.sleep(2)
#                 autogui.keyUp("ctrl")
                
#     except:  # agar inme koi bhi error ata h
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()


# # # def hotword():
# # #     porcupine = None
# # #     paud = None
# # #     audio_stream = None  # for streaming audio in background with microphone
# # #     try:

# # #         # pre trained keywords
# # #         porcupine = pvporcupine.create(keywords=["jarvis","alexa"]) # these two are already trained
# # #         paud = pyaudio.PyAudio()
# # #         audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
# # #         # loop for streaming
# # #         while True:
# # #             # to keep microphone always on
# # #             keyword=audio_stream.read(porcupine.frame_length)
# # #             keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

# # #             # processing keyword comes from mic 
# # #             keyword_index=porcupine.process(keyword) # checking the keyword (either it is  jarvis or alexa)

# # #             # checking first keyword detected or not
# # #             if keyword_index>=0:
# # #                 print("hotword detected")

# # #                 # pressing shorcut key ctrl+j( jb hotword keyword milega to apne aap hi ye keys press ho jayenge)
# # #                 import pyautogui as autogui
# # #                 autogui.keyDown("ctrl")
# # #                 autogui.press("j")
# # #                 time.sleep(2)
# # #                 autogui.keyUp("ctrl")
                
# # #     except:  # agar inme koi bhi error ata h
# # #         if porcupine is not None:
# # #             porcupine.delete()
# # #         if audio_stream is not None:
# # #             audio_stream.close()
# # #         if paud is not None:
# # #             paud.terminate()

# # # hotword()


# # # import pvporcupine
# # # import pyaudio
# # # import struct
# # # import time
# # # import pyautogui

# # # def hotword():
# # #     porcupine = None
# # #     paud = None
# # #     audio_stream = None  # For streaming audio from the microphone
# # #     try:
# # #         # Initialize porcupine with pre-trained keywords (No access_key required)
# # #         porcupine = pvporcupine.create(keywords=["jarvis", "alexa"])

# # #         paud = pyaudio.PyAudio()
# # #         audio_stream = paud.open(
# # #             rate=porcupine.sample_rate,
# # #             channels=1,
# # #             format=pyaudio.paInt16,
# # #             input=True,
# # #             frames_per_buffer=porcupine.frame_length
# # #         )

# # #         print("Listening for hotword...")

# # #         # Continuous loop for hotword detection
# # #         while True:
# # #             keyword = audio_stream.read(porcupine.frame_length)
# # #             keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

# # #             # Process the audio to detect hotword
# # #             keyword_index = porcupine.process(keyword)
# # #             if keyword_index >= 0:
# # #                 print("Hotword detected!")

# # #                 # Simulate shortcut key press (CTRL+J)
# # #                 pyautogui.keyDown("ctrl")
# # #                 pyautogui.press("j")
# # #                 time.sleep(2)
# # #                 pyautogui.keyUp("ctrl")

# # #     except Exception as e:
# # #         print(f"Error: {e}")  # Print any exception for debugging

# # #     finally:
# # #         # Clean up resources
# # #         if porcupine is not None:
# # #             porcupine.delete()
# # #         if audio_stream is not None:
# # #             audio_stream.close()
# # #         if paud is not None:
# # #             paud.terminate()

# # # hotword()


# # import pvporcupine
# # import struct
# # import time
# # import pyaudio
# # import traceback

# # def hotword():
# #     porcupine = None
# #     paud = None
# #     audio_stream = None
# #     try:
# #         # Use built-in keyword for testing (replace with custom if needed)
# #         porcupine = pvporcupine.create(keywords=["picovoice", "jarvis"]) 
# #         paud = pyaudio.PyAudio()
        
# #         # Open audio stream
# #         audio_stream = paud.open(
# #             rate=porcupine.sample_rate,
# #             channels=1,
# #             format=pyaudio.paInt16,
# #             input=True,
# #             frames_per_buffer=porcupine.frame_length
# #         )
        
# #         print("Listening for hotwords...")

# #         # Stream audio
# #         while True:
# #             keyword = audio_stream.read(porcupine.frame_length)
# #             keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

# #             # Process the audio to detect keywords
# #             keyword_index = porcupine.process(keyword)

# #             if keyword_index >= 0:
# #                 print("Hotword detected!")

# #                 # Trigger keyboard shortcut (Ctrl + J)
# #                 import pyautogui as autogui
# #                 autogui.keyDown("ctrl")
# #                 autogui.press("j")
# #                 time.sleep(2)
# #                 autogui.keyUp("ctrl")
                
# #     except Exception as e:
# #         print("Error Occurred:")
# #         traceback.print_exc()
# #     finally:
# #         if porcupine is not None:
# #             porcupine.delete()
# #         if audio_stream is not None:
# #             audio_stream.close()
# #         if paud is not None:
# #             paud.terminate()

# # hotword()

# import eel
# import pygame
# import pywhatkit as kit
# import os
# import re
# import sys
# import sqlite3
# import subprocess  # subprocess is for macOS
# import webbrowser
# import time
# import pvporcupine
# import pyaudio
# import struct
# import pyautogui
# from backend.helper import extract_yt_term, remove_words
# from backend.config import ASSISTANT_NAME  
# from backend.command import speak  
# conn = sqlite3.connect('jarvis.db')  
# cursor = conn.cursor()  


# def findContact(query):

#     words_to_remove = [ASSISTANT_NAME, "make", "a", "to", "phone", "call", "send", "message", "whatsapp", "video"]
#     query = remove_words(query, words_to_remove)

#     try:
#         query = query.strip().lower()
#         cursor.execute("SELECT phone FROM contacts WHERE LOWER(name) LIKE ?", (f"%{query}%",))
#         results = cursor.fetchall() # fetching all the results of that name
#         print(results[0][0])
#         mobile_number_str = str(results[0][0]) # converting the number into string

#         if not mobile_number_str.startswith("+91"):
#             mobile_number_str = "+91" + mobile_number_str

#         return mobile_number_str, query
#     except:
#         speak("Not exist in contacts")
# #         return 0, 0
    

# # query = "Anurag"
# # phone,name = findContact(query)




# # def findContact(query):
# #     words_to_remove = [ASSISTANT_NAME, "make", "a", "to", "phone", "call", "send", "message", "whatsapp", "video"]
# #     query = remove_words(query, words_to_remove)

# #     try:
# #         query = query.strip().lower()
# #         cursor.execute("SELECT phone FROM contacts WHERE LOWER(name) LIKE ?", (f"%{query}%",))
# #         results = cursor.fetchall()  # Fetching all the results of that name

# #         if results:
# #             print(results[0][0])
# #             mobile_number_str = str(results[0][0])  # Converting the number into string

# #             if not mobile_number_str.startswith("+91"):
# #                 mobile_number_str = "+91" + mobile_number_str

# #             return mobile_number_str, query
# #         else:
# #             speak("Not exist in contacts")
# #             return 0, 0

# #     except Exception as e:
# #         print(f"Error: {e}")
# #         speak("Not exist in contacts")
# #         return 0, 0

# query = "Abhinav Home"
# phone, name = findContact(query)


# import sqlite3
# import subprocess

# # Path to your database
# DB_PATH = "jarvis.db"

# # Function to fetch contact from the database
# def get_contact(name):
#     try:
#         # Connect to the SQLite database
#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()
        
#         # Fetch phone number by contact name
#         cursor.execute("SELECT phone FROM contacts WHERE name = ?", (name,))
#         result = cursor.fetchone()
#         conn.close()
        
#         if result:
#             return result[0]  # Return phone number
#         else:
#             print(f"[!] No contact found for {name}")
#             return None
#     except sqlite3.Error as e:
#         print(f"[!] Database error: {e}")
#         return None

# # Function to call contact using FaceTime
# def call_contact(phone):
#     # AppleScript to initiate a FaceTime call
#     script = f'''
#     tell application "FaceTime"
#         activate
#         delay 2
#         tell application "System Events"
#             keystroke "{phone}"
#             delay 1
#             keystroke return
#             delay 1
#             keystroke return
#         end tell
#     end tell
#     '''
#     # Run the AppleScript
#     subprocess.run(["osascript", "-e", script])

# # Example Usage
# if __name__ == "__main__":
#     name = input("Enter the contact name to call: ")
#     phone = get_contact(name)
    
#     if phone:
#         print(f"[+] Calling {name} at {phone}...")
#         call_contact(phone)

