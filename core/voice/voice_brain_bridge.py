
from core.voice.stt_engine import stt_engine
from core.voice.tts_engine import tts_engine


class VoiceBrainBridge:

    def process(self, audio):

        speech = stt_engine.convert(
            audio
        )

        response = (
            "response generated for "
            + speech["text"]
        )

        voice = tts_engine.speak(
            response
        )

        return {
            "input": speech,
            "response": voice,
            "status": "VOICE_BRAIN_CONNECTED"
        }


voice_brain_bridge = VoiceBrainBridge()
