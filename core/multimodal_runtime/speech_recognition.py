

class SpeechRecognition:

    def recognize(self,audio):
        return {
            "speech":"recognized",
            "status":"SPEECH_RECOGNITION_ENGINE_ACTIVE"
        }


speech_recognition=SpeechRecognition()

