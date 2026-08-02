

class SolutionGenerator:

    def generate(self,problem):
        return {
            "problem":problem,
            "solution":"generated",
            "status":"AUTO_SOLUTION_GENERATION_ACTIVE"
        }


solution_generator=SolutionGenerator()

