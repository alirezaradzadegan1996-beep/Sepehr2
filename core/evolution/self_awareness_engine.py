
class SelfAwarenessEngine:

    def __init__(self):

        self.system = "Sepehr2"

        self.capabilities = {
            "memory": 80,
            "reasoning": 75,
            "learning": 80,
            "agents": 70,
            "tools": 85
        }


    def analyze(self):

        weak = []

        for name, score in self.capabilities.items():

            if score < 80:
                weak.append(name)


        return {

            "system": self.system,

            "capabilities":
                self.capabilities,

            "weak_points":
                weak,

            "analysis":
                "completed",

            "status":
                "SELF_AWARENESS_ACTIVE"
        }



self_awareness_engine = SelfAwarenessEngine()

