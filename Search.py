import re
import pywhatkit
import wikipedia
import webbrowser
from Jarvis_main import speak

def get_search_query(query):
    return re.sub(r"\b(search in google|search in youtube|search in wikipedia|jarvis)\b", "", query, flags=re.IGNORECASE).strip()

def search_google(query):
    import wikipedia as googleScrap
    search_query = get_search_query(query)
    if not search_query:
        speak("Please, sir, dictate your search query.")
        return
    
    speak("This is what I found in Google:")
    try:
        pywhatkit.search(search_query)
        result = googleScrap.summary(search_query, sentences=1)
        speak(result)
    
    except:
        speak("No speakable output available.")
    
def search_youtube(query):
    search_query = get_search_query(query)
    if not search_query:
        speak("Please, sir, dictate your search query.")
        return
    
    speak("This is what I found in YouTube.")
    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
    pywhatkit.playonyt(search_query)
    speak("Done, sir.")

def search_wikipedia(query):
    search_query = get_search_query(query)
    if not search_query:
        speak("Please, sir, dictate your search query.")
        return
    try:
        webbrowser.open(f"https://en.wikipedia.org/wiki/{search_query}")
        results = wikipedia.summary(search_query, sentences=2)
        speak("According to Wikipedia...")
        speak(results)
    except wikipedia.exceptions.PageError:
        speak("I couldn't find anything on Wikipedia.")
    except Exception:
        speak("Something went wrong with Wikipedia search.")
