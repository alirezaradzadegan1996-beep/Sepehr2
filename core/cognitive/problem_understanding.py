from core.knowledge.knowledge_brain import brain


class ProblemUnderstanding:


    def understand(self, problem):

        knowledge = brain.query(problem)


        return {

            "input": problem,

            "meaning": "understood",

            "knowledge": knowledge,

            "has_knowledge":
                knowledge.get("status") == "found",

            "status": "ready"

        }



problem_understanding = ProblemUnderstanding()
