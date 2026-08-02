
class NeedDiscoveryEngine:


    def __init__(self):

        self.needs = []



    def analyze(self, situation):

        needs = []


        if "reasoning" in situation.get("weak_points", []):

            needs.append("advanced_reasoning")


        if "agents" in situation.get("weak_points", []):

            needs.append("agent_improvement")


        if situation.get("user_request"):

            needs.append(
                "user_requested_capability"
            )


        self.needs = needs


        return {

            "input":
                situation,

            "discovered_needs":
                needs,

            "priority":
                "calculated",

            "status":
                "NEED_DISCOVERY_ACTIVE"
        }



need_discovery_engine = NeedDiscoveryEngine()

