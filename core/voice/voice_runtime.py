
from core.voice.voice_input import voice_input
from core.voice.voice_processor import voice_processor
from core.interface.sepehr_terminal import sepehr_terminal


class VoiceRuntime:

    def run(self, audio):

        voice = voice_input.receive(
            audio
        )

        processed = voice_processor.process(
            voice
        )

        response = sepehr_terminal.send(
            processed["intent"]
        )

        return {
            "voice": voice,
            "processed": processed,
            "response": response,
            "status": "VOICE_ACTIVE"
        }


voice_runtime = VoiceRuntime()
