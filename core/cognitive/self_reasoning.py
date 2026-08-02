from core.cognitive.concept_comparison_reasoning import concept_comparison_reasoning


class SelfReasoning:

    def analyze(self, problem):

        text = problem.get(
            "input",
            ""
        )

        comparison = concept_comparison_reasoning.analyze(text)

        if comparison and comparison.get("knowledge_used"):
            return {
                "problem": problem,
                "knowledge_used": False,
                "reasoning_steps": [
                    "understand_problem",
                    "comparison_analysis"
                ],
                "conclusion": comparison["answer"],
                "analysis": "completed",
                "status": "reasoned"
            }


        knowledge = problem.get(
            "knowledge",
            {}
        )

        has_knowledge = problem.get(
            "has_knowledge",
            False
        )


        steps = [
            "understand_problem"
        ]


        if has_knowledge:

            steps.append(
                "use_existing_knowledge"
            )

            conclusion = knowledge.get(
                "answer"
            )


        else:

            steps.append(
                "reason_without_knowledge"
            )

            conclusion = self.generate_reasoned_answer(
                text
            )


        return {
            "problem": problem,
            "knowledge_used": has_knowledge,
            "reasoning_steps": steps,
            "conclusion": conclusion,
            "analysis": "completed",
            "status": "reasoned"
        }



    def generate_reasoned_answer(self, text):

        return (
            "تحلیل سپهر:\n"
            f"{text} یک موضوع قابل بررسی است.\n\n"
            "مقایسه:\n"
            "1- کاربرد\n"
            "2- ساختار\n"
            "3- مزایا\n"
            "4- محدودیت‌ها\n\n"
            "نتیجه: تفاوت‌ها بر اساس هدف و شرایط استفاده مشخص می‌شوند."
        )


self_reasoning = SelfReasoning()
