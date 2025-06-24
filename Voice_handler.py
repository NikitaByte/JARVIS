import pyttsx3
import speech_recognition
from colorama import Fore, Style, init
import time
from Config import lang

init()


def create_engine(rate=350, voice_index=0):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[voice_index].id)
    engine.setProperty("rate", rate)
    return engine

def speak(audio):
    engine.say(audio)
    print(Style.BRIGHT + "Jarvis : " + Style.RESET_ALL + audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print(Fore.YELLOW + "Listening...\r" + Style.RESET_ALL, end="", flush=True)
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print(Fore.YELLOW + "Processing...\r" + Style.RESET_ALL, end="", flush=True)
        query = r.recognize_google(audio)
        # if not lang == "en-US":
            # from Utilities import auto_translate
            # query = auto_translate(query)
        print(f"Recognized: {query}.")
    except speech_recognition.UnknownValueError:
        print(Fore.RED + "Voice recognition failed." + Style.RESET_ALL)
        return "none"
    except speech_recognition.RequestError:
        print(Fore.RED + "Error connecting to the recognition service." + Style.RESET_ALL)
        return "none"
    except speech_recognition.WaitTimeoutError:
        print(Fore.RED + "The waiting time is over." + Style.RESET_ALL)
        return "none"
    return query

engine = create_engine()