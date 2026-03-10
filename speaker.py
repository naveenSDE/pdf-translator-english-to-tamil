from gtts import gTTS
import pygame
import time

def speak_text(text):
    try:
        tts = gTTS(text=text, lang="ta")
        tts.save("static/voice.mp3")

        pygame.mixer.init()
        pygame.mixer.music.load("voice.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)

        return "voice.mp3"

    except Exception as e:
        print("error : cannot speak", e)
        return False