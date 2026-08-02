class SolutionGenerator:

    def generate(self, analysis):

        knowledge = None

        try:
            knowledge = (
                analysis
                .get("problem", {})
                .get("knowledge")
            )

        except Exception:
            pass


        if knowledge and knowledge.get("status") == "found":

            answer = knowledge.get(
                "answer",
                "دانشی پیدا نشد."
            )

            solution = (
                "بر اساس دانش موجود:\n"
                + answer
            )

        else:

            solution = (
                "تحلیل انجام شد. "
                "برای پاسخ دقیق‌تر نیاز به اطلاعات بیشتری دارم."
            )


        return {
            "analysis": analysis,
            "solution": solution,
            "status": "created"
        }


solution_generator = SolutionGenerator()
