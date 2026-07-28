from core.services.android_service import android_service


class AndroidCapability:

    name = "android"

    def can_handle(self, text):
        return android_service.can_handle(text)

    def handle(self, text):
        return android_service.handle(text)


capability = AndroidCapability()
