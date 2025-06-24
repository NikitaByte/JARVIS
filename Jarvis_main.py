import os
import datetime
from Voice_handler import takeCommand, speak
from colorama import Fore, Style, init
from Utilities import auto_translate

init()

def clear_console():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def main_loop():
        while True:
            query = takeCommand().lower()
            if "wake up" in query:
                from GreetMe import greetMe
                greetMe()

                while True:
                    query = takeCommand().lower()
                    if "go to sleep" in query:
                        speak("Ok sir, You can call me any time.")
                        break

                    elif query == "help":
                        help_text = """Commands:
- wake up: wake up the assistant
- hello: say hello to the assistant
- i am fine / i'm fine: tell the assistant your mood
- how are you: ask the assistant about their mood
- thank you: say "thank you"
- google <query>: search for a query in Google, opens the Google page
- youtube <query>: search for a query in YouTube, opens the YouTube page
- wikipedia <query>: search for a query in Wikipedia, opens the Wikipedia page
- clear console: clearing console
- time: getting current time
- finally sleep / over: turn off the program"""

                        print(help_text)

                    elif "hello" in query:
                        speak("Hello sir, how are you?")
                    elif "i am fine" in query or "i'm fine" in query :
                        speak("That's great, sir.")
                    elif "how are you" in query:
                        speak("Great, sir.")
                    elif "thank you" in query:
                        speak("You are welcome, sir.")

                    elif query.startswith("open"):
                        from Dictapp import open_app_web
                        open_app_web(query)
                    elif query.startswith("close"):
                        from Dictapp import close_app_web
                        close_app_web(query)

                    elif "google" in query:
                        from Search import search_google
                        search_google(query)
                    elif "youtube" in query:
                        from Search import search_youtube
                        search_youtube(query)
                    elif "wikipedia" in query:
                        from Search import search_wikipedia
                        search_wikipedia(query)

                    elif "clear console" in query:
                        clear_console()

                    elif "time" in query:
                        strTime = datetime.datetime.now().strftime("%H:%M")
                        speak(f"Sir, the time is {strTime}.")

                    elif query.startswith("translate"):
                        parts = query.replace("translate", "").strip().split(" ", 1)
                        if len(parts) == 2:
                            target_lang_word, text = parts
                            text = text.strip()

                            lang_map = {
                                "ukrainian": "uk",
                                "english": "en",
                                "french": "fr",
                                "german": "de",
                                "spanish": "es",
                                "polish": "pl"
                            }

                            target_lang = lang_map.get(target_lang_word.lower())
                            if target_lang:
                                translated = auto_translate(text, target_lang)
                                speak(f"Translated to {target_lang_word}: {translated}.")
                            else:
                                speak("Sorry, I don't support that language yet.")
                        else:
                            speak("Please say something like 'translate ukrainian Hello my friend'.")

                    elif "finally sleep" in query or "over" in query:
                        speak("Going to sleep, sir")
                        exit()

                    else:
                        if query != "none":
                            print(Fore.RED + "Invalid command." + Style.RESET_ALL)
                        print("Try \"help\" to show the command list.\n")
            else:
                if query != "none":
                    print(Fore.RED + "Invalid command." + Style.RESET_ALL)
                print("\"wake up\" to launch.\n")

if __name__ == "__main__":
    main_loop()