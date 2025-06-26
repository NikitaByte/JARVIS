import pyttsx3
import speech_recognition as sr
from Utilities import clear_console_line
from colorama import Fore, Style, init

init()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 250)

r = sr.Recognizer()


def speak(audio):
    engine.say(audio)
    print(Style.BRIGHT + "Jarvis : " + Style.RESET_ALL + audio)
    engine.runAndWait()

def takeCommand():
    with sr.Microphone() as source:
        print(Fore.YELLOW + "Listening...\r" + Style.RESET_ALL, end="", flush=True)
        r.adjust_for_ambient_noise(source, duration=0.2)
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        clear_console_line()
        print(Fore.YELLOW + "Processing...\r" + Style.RESET_ALL, end="", flush=True)
        query = r.recognize_google(audio)
        clear_console_line()
        print(f"Recognized: {query}.")
    except sr.UnknownValueError:
        print(Fore.RED + "Voice recognition failed." + Style.RESET_ALL)
        return "none"
    except sr.RequestError:
        print(Fore.RED + "Error connecting to the recognition service." + Style.RESET_ALL)
        return "none"
    except sr.WaitTimeoutError:
        print(Fore.RED + "The waiting time is over." + Style.RESET_ALL)
        return "none"
    return query