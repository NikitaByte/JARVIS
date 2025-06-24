import json

lang_modes = [ "en-US", "de-DE", "fr-FR", "es-ES", "it-IT", "uk-UA" ]
default_lang = "en-US"

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

lang = config["lang"]
if lang not in lang_modes:
    lang = default_lang