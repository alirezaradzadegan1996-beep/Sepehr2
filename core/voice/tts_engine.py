
class TTSEngine:

    def speak(self, text):

        return {
            "text": text,
            "audio": "generated_voice",
            "status": "spoken"
        }


tts_engine = TTSEngine()
