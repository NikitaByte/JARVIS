import pyttsx3
import datetime
import asyncio
from Voice_handler import speak

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def greetMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 3 and hour < 12:
        speak("Good Morning, sir.")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, sir.")
    else:
        speak("Good Evening, sir.")

    speak("Please tell me, how can I help you ?")