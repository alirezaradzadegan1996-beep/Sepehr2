"""
Sepehr2 Cortex Skill Manager
مدیریت چرخه زندگی Skill ها
"""

from core.skill_router import choose_skill


class SkillManager:

    def __init__(self, skills=None):
        self.skills = skills or []


    def register(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)


    def all(self):
        return self.skills


    def list(self):
        return [
            getattr(skill, "NAME", "Unknown")
            for skill in self.skills
        ]


    def count(self):
        return len(self.skills)


    def find(self, text, intent=None):

        # Direct Intent Routing
        if intent:

            for skill in self.skills:

                name = getattr(
                    skill,
                    "NAME",
                    ""
                ).lower()


                if intent == "math" and name == "math":
                    return skill


                if intent == "project" and name == "project":
                    return skill


                if intent == "greeting" and name == "greeting":
                    return skill


                if intent == "memory" and name == "memory":
                    return skill



        # Smart Routing

        skill, confidence = choose_skill(
            text,
            self.skills
        )


        if skill and confidence >= 0.5:
            return skill


        return None
