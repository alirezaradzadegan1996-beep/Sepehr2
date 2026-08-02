
class UpgradeExecutor:

    def execute(self, policy):

        return {
            "policy": policy,
            "upgrade": "completed",
            "status": "executed"
        }


upgrade_executor_upgrade = UpgradeExecutor()
