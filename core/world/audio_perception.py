
class AudioPerception:

    def process(self, audio):
        return {
            "audio": audio,
            "status": "processed"
        }

audio_perception = AudioPerception()
