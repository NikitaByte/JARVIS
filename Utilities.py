from langdetect import detect, detect_langs
from deep_translator import GoogleTranslator

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