from core.skill_router import choose_skill
from core.knowledge import search_knowledge
from core.ai_brain import think


class SkillEngine:

    def __init__(self, memory=None, cortex=None):

        self.memory = memory
        self.cortex = cortex


    def execute(self, plan):

        text = plan.get(
            "task",
            ""
        )

        intent = plan.get(
            "intent",
            ""
        )

        print("[SkillEngine] Input:", text)
        print("[SkillEngine] Intent:", intent)


        # دریافت Skill ها از Cortex
        skills = []

        if self.cortex:

            try:
                skills = self.cortex.get("skills")

            except Exception:
                skills = []


        # اگر Cortex هنوز Skills نداشت
        if not skills:

            from core.skill_registry import get_skills

            skills = get_skills()



        # -------------------------
        # Direct Intent Routing
        # -------------------------

        for skill in skills:

            name = getattr(
                skill,
                "NAME",
                ""
            )


            if intent == "greeting" and name == "Greeting":

                return skill.run(text)


            if intent == "memory" and name == "Memory":

                return skill.run(text)



        # -------------------------
        # Math
        # -------------------------

        if intent == "math":

            for skill in skills:

                if getattr(skill, "NAME", "") == "Math":

                    return skill.run(text)



        # -------------------------
        # Project
        # -------------------------

        if intent == "project":

            for skill in skills:

                if getattr(skill, "NAME", "") == "Project":

                    return skill.run(text)



        # -------------------------
        # Normal Skill Search
        # -------------------------

        skill, confidence = choose_skill(
            text,
            skills
        )


        if skill and confidence >= 0.5:

            return skill.run(text)



        # -------------------------
        # Knowledge
        # -------------------------

        answer = search_knowledge(text)


        if answer:

            print("[FALLBACK] Knowledge")

            return answer



        # -------------------------
        # AI
        # -------------------------

        print("[FALLBACK] AI")


        answer = think(text)


        from core.ai_learning import save_ai_answer


        save_ai_answer(
            text,
            answer
        )


        return answer
