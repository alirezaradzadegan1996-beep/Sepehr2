class SolutionGenerator:


    def generate(self, analysis):


        conclusion = analysis.get(
            "conclusion"
        )


        knowledge_used = analysis.get(
            "knowledge_used",
            False
        )


        if conclusion and knowledge_used:

            solution = (
                "بر اساس تحلیل سپهر:\n"
                + str(conclusion)
            )


        elif conclusion:

            solution = str(
                conclusion
            )


        else:

            solution = (
                "تحلیل انجام شد، "
                "اما اطلاعات کافی برای پاسخ وجود ندارد."
            )


        return {

            "analysis": analysis,

            "solution": solution,

            "status": "created"

        }



solution_generator = SolutionGenerator()
