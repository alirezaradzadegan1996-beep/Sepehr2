

class DeploymentManager:

    def deploy(self,product):
        return {
            "product":product,
            "deployment":"active",
            "status":"DEPLOYMENT_MANAGER_ACTIVE"
        }


deployment_manager=DeploymentManager()

