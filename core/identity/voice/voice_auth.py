from core.identity.voice.voice_profile import voice_profile


class VoiceAuth:


    def verify(self, signature):

        profile = voice_profile.get_voice()


        if (
            profile.get("registered")
            and profile.get("signature") == signature
        ):

            return {
                "access": True,
                "level": "OWNER",
                "confidence": 1.0,
                "status": "VOICE_VERIFIED"
            }


        return {
            "access": False,
            "level": "UNKNOWN",
            "confidence": 0.0,
            "status": "VOICE_REJECTED"
        }



voice_auth = VoiceAuth()
