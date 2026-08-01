from core.memory.experience_analyzer import experience_analyzer


class ExperienceGuidedDecision:


    def suggest(self, skill):


        analysis = experience_analyzer.analyze(
            skill
        )


        if analysis["count"] > 0:


            return {

                "skill": skill,

                "has_experience": True,

                "recommendation":
                analysis["experiences"][0]["lesson"]

            }


        return {

            "skill": skill,

            "has_experience": False,

            "recommendation":
            "no previous experience"

        }



experience_guided_decision = ExperienceGuidedDecision()
