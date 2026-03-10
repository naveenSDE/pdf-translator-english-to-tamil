from deep_translator import GoogleTranslator

def translate_text(text):
    try:
        translated = GoogleTranslator(
        source="en",
        target="ta").translate(text)
        return translated
    except Exception as e:
        print("translation : error",e)
        return ""
