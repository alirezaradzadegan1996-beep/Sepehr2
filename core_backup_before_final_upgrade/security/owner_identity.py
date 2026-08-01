from datetime import datetime


class OwnerIdentity:

    def __init__(self):

        self.owner = "Alireza"
        self.voice_registered = False
        self.face_registered = False


    def register_voice(self):

        self.voice_registered = True

        return {
            "owner": self.owner,
            "voice": "registered",
            "status": "active"
        }


    def register_face(self):

        self.face_registered = True

        return {
            "owner": self.owner,
            "face": "registered",
            "status": "active"
        }


    def verify(self, voice, face):

        if self.voice_registered and self.face_registered:

            return {
                "identity": self.owner,
                "voice_match": voice,
                "face_match": face,
                "access": "full",
                "status": "verified"
            }

        return {
            "access":"limited",
            "status":"not_verified"
        }



identity = OwnerIdentity()


print(
    identity.register_voice()
)

print(
    identity.register_face()
)

print(
    identity.verify(
        "matched",
        "matched"
    )
)


print(
    {
        "status":"owner_identity_layer_active",
        "time":str(datetime.now())
    }
)

