

class UpgradeDeployment:

    def deploy(self,upgrade):
        return {
            "upgrade":upgrade,
            "deployment":"completed",
            "status":"AUTO_UPGRADE_DEPLOYMENT_ACTIVE"
        }


upgrade_deployment=UpgradeDeployment()

