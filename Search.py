import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
from Jarvis_main import takeCommand, speak

def search_google(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found in Google.")
    
    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query,1)
        speak(result)
    
    except:
        speak("No speakable output available.")
    
def search_youtube(query):
    if "youtube" in query:
        query = query.replace("jarvis", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube", "")
        speak("This is what I found in YouTube.")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, sir.")

def search_wikipedia(query):
    speak("Searching from Wikipedia...")
    query = query.replace("jarvis", "")
    query = query.replace("wikipedia search", "")
    query = query.replace("wikipedia", "")
    web = "https://en.wikipedia.org/wiki/" + query
    webbrowser.open(web)
    results = wikipedia.summary(query, sentences = 2)
    speak("According to Wikipedia...")
    if results:
        speak(results)


