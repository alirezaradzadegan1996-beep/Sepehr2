from datetime import datetime


class VoiceConversation:


    def __init__(self):

        self.owner = "Alireza"
        self.history = []



    def speech_to_text(self, audio):

        return {
            "audio": audio,
            "text": "سلام سپهر",
            "language": "fa",
            "status": "converted"
        }



    def understand_voice(self, text):

        return {
            "input": text,
            "intent": "conversation",
            "status": "understood"
        }



    def text_to_speech(self, response):

        return {
            "text": response,
            "voice": "Sepehr_voice",
            "status": "generated"
        }



    def process(self, audio):

        speech = self.speech_to_text(audio)

        context = self.understand_voice(
            speech["text"]
        )

        response = "سلام علیرضا، سپهر آماده است."

        voice = self.text_to_speech(
            response
        )

        self.history.append(
            {
                "input": speech,
                "response": voice
            }
        )


        return {
            "speech": speech,
            "context": context,
            "response": voice,
            "memory_count": len(self.history)
        }



voice = VoiceConversation()


print(
    voice.process(
        "simulated_voice"
    )
)


print(
    {
        "status":"voice_conversation_active",
        "time":str(datetime.now())
    }
)

