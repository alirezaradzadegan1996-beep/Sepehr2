import os

def speak(text):
    os.system(f'termux-tts-speak "{text}"')


def listen():
    return os.popen("termux-speech-to-text").read().strip()
