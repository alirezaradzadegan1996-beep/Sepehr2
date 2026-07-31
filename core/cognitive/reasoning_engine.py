class ReasoningEngine:


    def analyze(self, problem):

        return {
            "problem":problem,
            "reasoning":[
                "analyze",
                "compare",
                "conclude"
            ],
            "status":"reasoned"
        }


reasoning_engine = ReasoningEngine()
