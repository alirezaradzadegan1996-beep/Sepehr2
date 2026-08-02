class PatchGenerator:

    def generate(self, plan):

        patches = []

        for item in plan.get("plans", []):

            solution = item.get("solution")

            if solution == "upgrade_reasoning_engine":

                patches.append({
                    "target":
                    "core/cognitive/self_reasoning.py",

                    "change":
                    "add reasoning pattern improvement",

                    "reason":
                    "weak reasoning response",

                    "risk":
                    "medium"
                })


            elif solution == "expand_knowledge":

                patches.append({
                    "target":
                    "data/knowledge.json",

                    "change":
                    "add missing knowledge entries",

                    "reason":
                    "knowledge gap",

                    "risk":
                    "low"
                })


            elif solution == "improve_reasoning_quality":

                patches.append({
                    "target":
                    "core/cognitive",

                    "change":
                    "optimize reasoning templates",

                    "reason":
                    "low confidence answers",

                    "risk":
                    "medium"
                })


        return {
            "status":"patch_generated",
            "patches":patches,
            "count":len(patches)
        }


patch_generator = PatchGenerator()
