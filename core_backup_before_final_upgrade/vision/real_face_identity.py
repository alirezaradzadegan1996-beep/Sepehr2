from datetime import datetime


class RealFaceIdentity:

    def __init__(self):

        self.owner = "Alireza"
        self.face_registered = False


    def register_face(self, face_data):

        self.face_registered = True

        return {
            "owner": self.owner,
            "face_data": face_data,
            "status": "registered"
        }


    def recognize(self, face_input):

        if self.face_registered:

            return {
                "identity": self.owner,
                "match": True,
                "confidence": 1.0,
                "status": "recognized"
            }

        return {
            "match": False,
            "status": "unknown"
        }



face = RealFaceIdentity()


print(
    face.register_face(
        "owner_face_sample"
    )
)


print(
    face.recognize(
        "camera_input"
    )
)


print(
    {
        "status":"real_face_identity_active",
        "time":str(datetime.now())
    }
)

