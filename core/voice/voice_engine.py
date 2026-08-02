

class VoiceEngine:

    def listen(self):

        return {
            "voice":"received",
            "status":"VOICE_INPUT_ACTIVE"
        }


    def speak(self,text):

        return {
            "response":text,
            "status":"VOICE_OUTPUT_ACTIVE"
        }


voice_engine=VoiceEngine()

