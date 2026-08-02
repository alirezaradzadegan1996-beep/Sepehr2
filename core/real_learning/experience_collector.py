

class ExperienceCollector:

    def collect(self, experience):

        return {
            "experience": experience,
            "collected": True,
            "status": "EXPERIENCE_COLLECTION_ACTIVE"
        }


experience_collector = ExperienceCollector()

