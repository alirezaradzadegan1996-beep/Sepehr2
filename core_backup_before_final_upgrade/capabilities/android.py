from core.services.android_service import android_service


class AndroidCapability:

    name = "android"


    def score(self, text):

        score = 0

        keywords = {
            "باتری": 20,
            "battery": 20,
            "wifi": 20,
            "وای فای": 20,
            "دوربین": 20,
            "camera": 20,
            "عکس": 20,
            "سنسور": 20,
            "موقعیت": 20,
            "gps": 20,
            "صدا": 20,
            "اعلان": 20,
            "کلیپ": 20,
            "فایل": 10,
            "پوشه": 10
        }

        for key, value in keywords.items():

            if key in text.lower():
                score += value

        return score


    def can_handle(self, text):

        return self.score(text) > 0


    def handle(self, text):

        return android_service.handle(text)


capability = AndroidCapability()
