

class ExperienceStorage:

    def save(self,experience):
        return {
            "experience":experience,
            "storage":"completed",
            "status":"EXPERIENCE_STORAGE_CORE_ACTIVE"
        }


experience_storage=ExperienceStorage()

