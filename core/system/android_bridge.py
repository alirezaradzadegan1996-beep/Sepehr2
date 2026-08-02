
from core.system.command_executor import command_executor


class AndroidBridge:

    def run_action(self, action):

        result = command_executor.execute(
            action
        )

        return {
            "action": action,
            "system": result,
            "status": "ANDROID_CONNECTED"
        }


android_bridge = AndroidBridge()
