

class SpeechProcessing:

    def process(self,text):
        return {
            "speech":text,
            "processed":True,
            "status":"SPEECH_PROCESSING_LAYER_ACTIVE"
        }


speech_processing=SpeechProcessing()

