

class CapabilityPriorityEngine:


    def prioritize(self, weaknesses):

        return {

            "priority":
                weaknesses[0] if weaknesses else None,

            "queue":
                weaknesses,

            "status":
                "CAPABILITY_PRIORITY_ACTIVE"

        }



capability_priority_engine = CapabilityPriorityEngine()

