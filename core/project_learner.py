import time

from core.experience_memory import ExperienceMemory


class ProjectLearner:

    def __init__(self):

        self.memory = ExperienceMemory()


    def learn_from_project(self, project):

        if not project:
            return {
                "learned": False,
                "reason": "no project"
            }


        analysis = project.get(
            "analysis",
            {}
        )


        project_type = analysis.get(
            "type",
            "general"
        )


        files = analysis.get(
            "files",
            []
        )


        features = analysis.get(
            "features",
            []
        )


        test_result = project.get(
            "test_result",
            {}
        )


        success = False


        if isinstance(test_result, dict):

            success = test_result.get(
                "success",
                False
            )

        elif isinstance(test_result, str):

            success = (
                "موفق" in test_result
                or
                "passed" in test_result
            )


        experience = {

            "project_type": project_type,

            "project_id": project.get(
                "id"
            ),

            "name": project.get(
                "goal"
            ),

            "files": files,

            "features": features,

            "success": success,

            "score": 100 if success else 0,

            "time": time.time()
        }


        if success:

            self.memory.learn_from_project(
                project
            )


        return {
            "learned": True,
            "success": success,
            "experience": experience
        }
