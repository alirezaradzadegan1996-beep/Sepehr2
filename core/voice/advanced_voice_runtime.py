
from core.voice.voice_brain_bridge import voice_brain_bridge


class AdvancedVoiceRuntime:

    def run(self, audio):

        return voice_brain_bridge.process(
            audio
        )


advanced_voice_runtime = AdvancedVoiceRuntime()
