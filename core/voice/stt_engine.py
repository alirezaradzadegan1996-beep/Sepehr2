
class STTEngine:

    def convert(self, audio):

        return {
            "audio": audio,
            "text": "converted speech text",
            "status": "recognized"
        }


stt_engine = STTEngine()
