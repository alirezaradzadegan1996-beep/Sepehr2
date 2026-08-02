

class VoiceResponse:

    def generate(self,text):
        return {
            "response":"generated",
            "status":"VOICE_RESPONSE_GENERATOR_ACTIVE"
        }


voice_response=VoiceResponse()

