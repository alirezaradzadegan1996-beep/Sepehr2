

class VoiceInput:

    def listen(self):

        return {

            "audio":
            "received",

            "status":
            "VOICE_INPUT_ACTIVE"

        }



class SpeechProcessor:

    def process(self,audio):

        return {

            "text":
            "processed",

            "status":
            "SPEECH_PROCESSING_ACTIVE"

        }



class VoiceOutput:

    def speak(self,text):

        return {

            "output":
            text,

            "status":
            "VOICE_OUTPUT_ACTIVE"

        }



voice_input=VoiceInput()
speech_processor=SpeechProcessor()
voice_output=VoiceOutput()

