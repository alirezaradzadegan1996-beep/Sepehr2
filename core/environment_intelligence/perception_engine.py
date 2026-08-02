

class PerceptionEngine:

    def scan(self,environment):
        return {
            "environment":environment,
            "signals":"collected",
            "status":"ENVIRONMENT_PERCEPTION_ACTIVE"
        }


perception_engine=PerceptionEngine()

