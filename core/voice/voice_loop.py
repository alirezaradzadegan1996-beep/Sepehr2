from core.voice.voice_engine import VoiceEngine


class VoiceLoop:

    def __init__(self, kernel):
        self.voice = VoiceEngine()
        self.kernel = kernel
        self.active = False

    def run(self):

        print("🧠 Voice system started...")

        while True:
            text = self.voice.listen()

            if not text:
                continue

            # فعال شدن با wake word
            if self.voice.is_wake_word(text):
                self.active = True
                text = self.voice.remove_wake_word(text)
                print("🚀 Activated")

            if self.active:
                if text:
                    result = self.kernel.process(text)
                    print("🤖", result)

                # خاموش شدن ساده
                if "خداحافظ" in text:
                    print("👋 Sleeping mode")
                    self.active = False
