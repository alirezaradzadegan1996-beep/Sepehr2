import json
from core.experience_memory import ExperienceMemory


class CodeEvolution:

    def __init__(self):
        self.memory = ExperienceMemory()


    def evolve(self, project_type, files, features=None):

        experience = self.memory.get_best_practices(
            project_type
        )

        result = {
            "original_files": files,
            "added_files": [],
            "features": [],
            "experience_used": False,
            "confidence": "none"
        }


        if not experience.get("found"):
            return result


        confidence = experience.get(
            "confidence",
            "low"
        )

        result["confidence"] = confidence


        if confidence == "low":
            return result


        learned_files = experience.get(
            "files",
            []
        )


        for file in learned_files:

            if file not in files:
                result["added_files"].append(
                    file
                )


        result["features"] = experience.get(
            "features",
            []
        )


        result["experience_used"] = True


        return result



    def apply(self, project_type, files):

        evolution = self.evolve(
            project_type,
            files
        )


        final_files = list(files)


        for file in evolution.get(
            "added_files",
            []
        ):

            if file not in final_files:
                final_files.append(
                    file
                )


        # Dependency rules
        dependencies = {

            "calculator": [
                "history.py",
                "validator.py",
                "errors.py",
                "operations.py"
            ],

            "robot": [
                "sensor.py",
                "motor.py",
                "brain.py"
            ],

            "ai_agent": [
                "memory.py",
                "learner.py",
                "decision.py"
            ]

        }


        for dependency in dependencies.get(
            project_type,
            []
        ):

            if dependency not in final_files:

                final_files.append(
                    dependency
                )


        evolution["dependency_added"] = list(
            set(final_files) - set(files)
        )


        return {
            "files": final_files,
            "evolution": evolution
        }
