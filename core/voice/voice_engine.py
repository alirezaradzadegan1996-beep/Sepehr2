import speech_recognition as sr


class VoiceEngine:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.wake_word = "سپهر"

    def listen(self):
        with sr.Microphone() as source:
            print("🎤 Listening...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="fa-IR")
            print("🧾 Heard:", text)
            return text
        except:
            return ""

    def is_wake_word(self, text):
        return self.wake_word in text

    def remove_wake_word(self, text):
        return text.replace(self.wake_word, "").strip()
