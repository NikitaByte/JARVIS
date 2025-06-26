import platform
import os
import psutil
import socket
from langdetect import detect, detect_langs
from deep_translator import GoogleTranslator

def remove_from_line(line, *words):
    for word in words:
        line = line.replace(word, "").strip()
    return line

def clear_console_line():
    print("\n\033[F\033[K", end="")

def wait_for_keypress():
    print("Press any key to continue...\r", end="", flush=True)
    if os.name == "nt":
        import msvcrt
        msvcrt.getch()
    else:
        import getch
        getch.getch()
    clear_console_line()

def auto_translate(text, target_lang = "en"):
    try:
        source_lang = detect(text)
        if source_lang == target_lang:
            print(f"The text is already in {target_lang}")
            return text
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated
    except Exception as ex:
        print(f"Error: {ex}")
        return text

def system_info():
    return f"""--- System information ---
System: {platform.system()}
Node name (PC name): {platform.node()}
Release: {platform.release()}
Version: {platform.version()}
Machine: {platform.machine()}
Processor: {platform.processor()}
CPU Cores: {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count()} logical
RAM: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB
Disk Usage: {psutil.disk_usage('/').percent}% used
Architecture: {platform.architecture()[0]}
Hostname: {socket.gethostname()}
IP Address: {socket.gethostbyname(socket.gethostname())}"""