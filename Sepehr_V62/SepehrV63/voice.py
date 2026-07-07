import os

# گفتار (TTS)
def speak(text):
    os.system(f'termux-tts-speak "{text}"')
