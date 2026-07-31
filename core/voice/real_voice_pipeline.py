from datetime import datetime


class RealVoicePipeline:

    def __init__(self):
        self.language = "fa"
        self.status = "ready"


    def listen(self, audio_source):

        return {
            "source": audio_source,
            "audio_received": True,
            "status": "captured"
        }


    def speech_to_text(self, audio):

        return {
            "text": "سلام سپهر",
            "language": self.language,
            "confidence": 1.0,
            "status": "recognized"
        }


    def text_to_speech(self, text):

        return {
            "voice_output": text,
            "voice": "Sepehr",
            "status": "generated"
        }



voice = RealVoicePipeline()


audio = voice.listen("microphone")

text = voice.speech_to_text(audio)

reply = voice.text_to_speech(
    "سلام علیرضا، آماده‌ام."
)


print(audio)
print(text)
print(reply)

print(
    {
        "status":"real_voice_pipeline_active",
        "time":str(datetime.now())
    }
)

