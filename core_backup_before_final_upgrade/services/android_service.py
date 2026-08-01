from core.device_control.android.android_manager import android_manager


class AndroidService:

    def initialize(self):
        pass


    def boot(self):
        print("[Android] Ready")


    def can_handle(self, text):

        keys = [
            "باتری",
            "battery",
            "دوربین",
            "عکس",
            "camera",
            "موقعیت",
            "gps",
            "wifi",
            "وای فای",
            "سنسور",
            "شتاب",
            "صدا",
            "ولوم",
            "اعلان",
            "کلیپ",
        ]

        t = text.lower()

        return any(k in t for k in keys)


    def handle(self, text):

        return android_manager.execute(text)


android_service = AndroidService()
