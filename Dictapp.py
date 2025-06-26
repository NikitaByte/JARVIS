import os
import pyautogui
import webbrowser
import re
import time
from Voice_handler import speak

dictapp = {
    "commandprompt" : "cmd",
    "paint" : "paint",
    "word" : "winword",
    "excel" : "excel",
    "chrome" : "chrome",
    "visual studio code" : "code",
    "powerpoint" : "powerpnt"
}

def open_app_web(query):
    speak("Launching, sir")
    cleaned_query = re.sub(r"\b(open|jarvis)\b", "", query, flags=re.IGNORECASE).strip()
    if any(ext in cleaned_query for ext in [".com", ".org"]):
        url = cleaned_query.replace(" ", "")
        webbrowser.open(f"https://www.{url}")
    else:
        for app in dictapp:
            if app in cleaned_query:
                os.system(f'start "" "{dictapp[app]}"')
                break
        else:
            speak("App not found, sir")

def close_app_web(query):
    speak("Closing, sir.")

    tab_map = {
        "one tab": 1, "1 tab": 1,
        "two tabs": 2, "2 tabs": 2,
        "three tabs": 3, "3 tabs": 3,
        "four tabs": 4, "4 tabs": 4,
        "five tabs": 5, "5 tabs": 5,
    }

    times = next((v for k, v in tab_map.items() if k in query), 0)
    
    if times > 0:
        for _ in range(times):
            pyautogui.hotkey("ctrl", "w")
            time.sleep(0.5)
        speak("Tabs closed")
        return
    
    closed_any = False
    for app, exe_name in dictapp.items():
        if app in query:
            os.system(f"taskkill /f /im {exe_name}.exe")
            closed_any = True
    
    if closed_any:
        speak("Apps closed.")
    else:
        speak("Unable to close anything, sir.")
            
    