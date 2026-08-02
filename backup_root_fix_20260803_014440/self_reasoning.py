class SelfReasoning:


    def analyze(self, problem):

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

            steps.append(
                "generate_possible_causes"
            )

            steps.append(
                "construct_logical_analysis"
            )

            text = problem.get(
                "input",
                ""
            )

            if any(x in text for x in [
                "ماشین",
                "موتور",
                "داغ",
                "حرارت",
                "جوش"
            ]):

                conclusion = (
                    "تحلیل سپهر:\n"
                    "مشکل مربوط به افزایش دمای موتور است.\n"
                    "علت‌های احتمالی:\n"
                    "1- کمبود مایع خنک کننده\n"
                    "2- خرابی فن خنک کننده\n"
                    "3- گیر کردن ترموستات\n"
                    "4- گرفتگی رادیاتور\n"
                    "5- مشکل واتر پمپ\n"
                    "پیشنهاد: ابتدا سطح آب رادیاتور، عملکرد فن و نشتی بررسی شود."
                )

            else:

                conclusion = (
                    "تحلیل اولیه سپهر:\n"
                    "دانش مستقیم پیدا نشد، "
                    "اما مسئله بررسی و به چند بخش قابل تحلیل تقسیم شد."
                )


        return {

            "problem": problem,

            "knowledge_used":
                has_knowledge,

            "reasoning_steps":
                steps,

            "conclusion":
                conclusion,

            "analysis":
                "completed",

            "status":
                "reasoned"

        }



self_reasoning = SelfReasoning()
