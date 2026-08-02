
class VoiceInput:

    def receive(self, audio):

        return {
            "audio": audio,
            "text": "converted_text",
            "status": "converted"
        }


voice_input = VoiceInput()
