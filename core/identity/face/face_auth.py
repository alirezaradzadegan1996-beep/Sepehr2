from core.identity.face.face_profile import face_profile


class FaceAuth:


    def verify(self, signature):

        profile = face_profile.get_face()


        if (
            profile.get("registered")
            and profile.get("signature") == signature
        ):

            return {
                "access": True,
                "level": "OWNER",
                "confidence": 1.0,
                "status": "FACE_VERIFIED"
            }


        return {
            "access": False,
            "level": "UNKNOWN",
            "confidence": 0.0,
            "status": "FACE_REJECTED"
        }



face_auth = FaceAuth()
