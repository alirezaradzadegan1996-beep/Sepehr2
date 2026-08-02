
class LifecycleManager:

    def check(self):

        return {
            "services":"healthy",
            "monitor":"active",
            "status":"LIFECYCLE_MANAGER_ACTIVE"
        }


lifecycle_manager = LifecycleManager()
