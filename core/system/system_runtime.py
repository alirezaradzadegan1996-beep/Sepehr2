
from core.system.file_manager import file_manager
from core.system.android_bridge import android_bridge


class SystemRuntime:

    def run(self, request):

        file = file_manager.create(
            "data/system_test.txt",
            "sepehr system test"
        )

        android = android_bridge.run_action(
            request
        )

        return {
            "file": file,
            "android": android,
            "status": "SYSTEM_ACTIVE"
        }


system_runtime = SystemRuntime()
