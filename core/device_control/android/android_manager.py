from .android_service import AndroidService


class AndroidManager:

    def __init__(self):
        self.android = AndroidService()


    def info(self):
        return {
            "name": "android_manager",
            "status": "ready",
            "features": self.android.info()
        }


    def execute(self, command):
        return self.android.execute(command)


android_manager = AndroidManager()
