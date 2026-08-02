

class UpgradeManager:

    def upgrade(self,capability):
        return {
            "capability":capability,
            "upgrade":"completed",
            "status":"SELF_UPGRADE_MANAGER_ACTIVE"
        }


upgrade_manager=UpgradeManager()

