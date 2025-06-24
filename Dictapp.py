import os
import pyautogui
import webbrowser
import pyttsx3
import time
from Voice_handler import takeCommand, speak

dictapp = {
    "commandprompt" : "cmd",
    "paint" : "paint",
    "word" : "winword",
    "excel" : "excel",
    "chrome" : "chrome",
    "vscode" : "code",
    "powerpoint" : "powerpnt"
}

def open_app_web(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "").strip()
        query = query.replace("launch", "").strip()
        query = query.replace("jarvis", "").strip()
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def close_app_web(query):
    speak("Closing, sir.")
    times = 0
    if "one tab" in query or "1 tab" in query:
        times = 1
    elif "two tabs" "2 tabs" in query:
        times = 2
    elif "three tabs" "3 tabs" in query:
        times = 3
    elif "four tabs" "4 tabs" in query:
        times = 4
    elif "five tabs" "5 tabs" in query:
        times = 5
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
    for i in range(times):
        pyautogui.hotkey("ctrl", "w")
        time.sleep(0.5)
    speak("All tabs closed.")