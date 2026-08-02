class ExperienceNormalizer:

    def normalize(self, experience):

        if not isinstance(experience, dict):
            return {
                "goal": str(experience),
                "input": str(experience),
                "skill": "unknown",
                "success": False,
                "source": "legacy"
            }

        return {
            "goal": (
                experience.get("goal")
                or experience.get("input")
                or experience.get("data")
                or experience.get("text")
                or "unknown"
            ),

            "input": (
                experience.get("input")
                or experience.get("data")
                or experience.get("text")
                or experience.get("goal")
                or "unknown"
            ),

            "skill": experience.get(
                "skill",
                "unknown"
            ),

            "success": (
                experience.get("success", False)
                or experience.get("result") == "success"
            ),

            "source": experience.get(
                "source",
                "experience_memory"
            ),
            "response": experience.get(
                "response",
                None
            )
        }


experience_normalizer = ExperienceNormalizer()
