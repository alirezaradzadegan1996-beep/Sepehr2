class PriorityReasoner:


    dependencies = {

        "camera": {
            "reason": "required by vision",
            "priority": 10
        },

        "vision": {
            "reason": "digital perception",
            "priority": 9
        },

        "voice_input": {
            "reason": "digital hearing",
            "priority": 8
        },

        "voice_output": {
            "reason": "digital speech",
            "priority": 7
        },

        "web": {
            "reason": "world connection",
            "priority": 6
        },

        "tools": {
            "reason": "external actions",
            "priority": 6
        },

        "learning": {
            "reason": "self improvement",
            "priority": 10
        }

    }


    def rank(self, tasks):

        ranked = []


        for task in tasks:

            skill = task.get("skill")


            info = self.dependencies.get(
                skill,
                {
                    "priority":5,
                    "reason":"unknown"
                }
            )


            ranked.append(
                {
                    "skill":skill,
                    "priority":info["priority"],
                    "reason":info["reason"]
                }
            )


        return sorted(
            ranked,
            key=lambda x:x["priority"],
            reverse=True
        )


priority_reasoner = PriorityReasoner()
