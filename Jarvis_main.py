import os
import datetime
from Utilities import remove_from_line, system_info, wait_for_keypress, auto_translate
from Voice_handler import takeCommand, speak
from colorama import Fore, Style, init

init()

def clear_console():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def main_loop():
        greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
        how_are_you = ["how are you", "how do you do", "how's it going"]
        thanks_list = ["thanks", "thank you", "i'm grateful", "i am grateful"]
        good_moods = ["fine", "ok", "great", "good", "amazing"]
        bad_moods = ["bad", "not good", "sad", "terrible", "depressed"]

        while True:
            query = takeCommand().lower()
            if "wake up" in query:
                from GreetMe import greetMe
                greetMe()

                while True:
                    query = takeCommand().lower()
                    query = remove_from_line(query, "jarvis", "please")

                    if "go to sleep" in query:
                        speak("Ok sir, You can call me any time.")
                        break

                    elif "help list" in query:
                        help_text = """Commands:
- wake up: wake up the assistant
- hello: say hello to the assistant
- i am fine / i'm fine: tell the assistant your mood
- how are you: ask the assistant about their mood
- thank you: say "thank you"
- google <query>: search for a query in Google, opens the Google page
- youtube <query>: search for a query in YouTube, opens the YouTube page
- wikipedia <query>: search for a query in Wikipedia, opens the Wikipedia page
- clear: clearing console
- time: getting current time
- system <task>: to shut down, restart, put to sleep or get info of the system (task: shutdown, reboot, sleep, info)
- finally sleep: turn off the program
- help list: show this list"""
                        print(help_text)

                    if any(query.startswith(greet) for greet in greetings):
                        speak("Hello sir, how are you?")
                    elif any(query.startswith(f"i'm {m}") or query.startswith(f"i am {m}") for m in good_moods):
                        speak("That's great, sir.")
                    elif any(query.startswith(f"i'm {m}") or query.startswith(f"i am {m}") for m in bad_moods):
                        speak("I hope that everything will get better with you, sir.")
                    elif any(query.startswith(how) for how in how_are_you):
                        speak("Great, sir.")
                    elif any(query.startswith(thx) for thx in thanks_list):
                        speak("You are welcome, sir.")

                    elif query.startswith("open"):
                        from Dictapp import open_app_web
                        open_app_web(query)
                    elif query.startswith("close"):
                        from Dictapp import close_app_web
                        close_app_web(query)

                    elif query.startswith("search in google"):
                        from Search import search_google
                        search_google(query)
                    elif query.startswith("search in youtube"):
                        from Search import search_youtube
                        search_youtube(query)
                    elif query.startswith("search in wikipedia"):
                        from Search import search_wikipedia
                        search_wikipedia(query)

                    elif query.startswith("clear"):
                        clear_console()

                    elif any(query.startswith(time_command) for time_command in ["time", "what is the time"]):
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

                    elif query.startswith("system"):
                        task = remove_from_line(query, "system")
                        if task == "shutdown":
                            choice = input("Do you wish to shutdown your computer? (y/n)\n> ")
                            if choice == "y":
                                    if os.name == "nt":
                                        _ = os.system("shutdown /s /t 0")
                                    else:
                                        _ = os.system("shutdown now")
                            elif choice == "n":
                                break
                            else:
                                print(Fore.RED + "Invalid command." + Style.RESET_ALL)
                        elif task == "reboot":
                            choice = input("Do you wish to restart your computer? (y/n)\n> ")
                            if choice == "y":
                                if os.name == "nt":
                                    _ = os.system("shutdown /r /t 0")
                                else:
                                    _ = os.system("reboot")
                            elif choice == "n":
                                break
                            else:
                                print(Fore.RED + "Invalid command." + Style.RESET_ALL)
                        elif task == "sleep":
                            choice = input("Do you wish to put your computer to sleep? (y/n)\n> ")
                            if choice == "y":
                                if os.name == "nt":
                                    _ = os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                                else:
                                    _ = os.system("systemctl suspend")
                            elif choice == "n":
                                break
                            else:
                                print(Fore.RED + "Invalid command." + Style.RESET_ALL)
                        elif task == "info":
                            info = system_info()
                            print(info)
                        else:
                            print("""Hint:
system shutdown
system reboot
system sleep
system info""")

                    elif query.startswith("wait"):
                        speak("I'm waiting, sir")
                        wait_for_keypress()

                    elif query.startswith("finally sleep"):
                        speak("Going to sleep, sir")
                        exit()

                    elif query.startswith("calculate"):
                        expression = remove_from_line(query, "calculate")
                        if not expression:
                            speak("Please, sir, dictate a mathematical expression.")
                        from Calculator import calc
                        result = calc(expression)
                        if result != None:
                            speak(f"Result is {result}.")

                    else:
                        if query != "none":
                            print(Fore.RED + "Invalid command." + Style.RESET_ALL)
                        print("Try \"help list\" to show the command list.\n")
            else:
                if query != "none":
                    print(Fore.RED + "Invalid command." + Style.RESET_ALL)
                print("\"wake up\" to launch.\n")

if __name__ == "__main__":
    main_loop()