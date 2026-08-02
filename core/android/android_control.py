
class AndroidControl:

    def execute(self, action):

        return {
            "action": action,
            "device": "connected",
            "result": "executed",
            "status": "ANDROID_CONTROL_ACTIVE"
        }


android_control = AndroidControl()
