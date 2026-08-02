
class VoiceUnderstanding:

    def understand(self, text):
        return {
            "meaning": text,
            "status": "understood"
        }

voice_understanding = VoiceUnderstanding()
