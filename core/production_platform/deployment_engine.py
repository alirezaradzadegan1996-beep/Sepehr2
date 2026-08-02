

class DeploymentEngine:

    def deploy(self,service):
        return {
            "service":service,
            "deployment":"completed",
            "status":"SERVICE_DEPLOYMENT_ACTIVE"
        }


deployment_engine=DeploymentEngine()

