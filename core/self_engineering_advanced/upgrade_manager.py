

class UpgradeManager:

    def upgrade(self,capability):
        return {
            "capability":capability,
            "upgrade":"deployed",
            "status":"UPGRADE_MANAGER_ACTIVE"
        }


upgrade_manager=UpgradeManager()

