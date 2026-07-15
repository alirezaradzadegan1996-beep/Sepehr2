from core.project_memory import ProjectMemory
from core.experience_memory import ExperienceMemory


class ExperienceConsolidator:

    def __init__(self):
        self.memory = ProjectMemory()
        self.experience_memory = ExperienceMemory()


    def consolidate(self, project):

        if not project:
            return {
                "updated": False,
                "reason": "empty project"
            }


        project_id = project.get(
            "id"
        )


        analysis = project.get(
            "analysis",
            {}
        )


        reasoning = analysis.get(
            "reasoning",
            {}
        )


        evolution = reasoning.get(
            "evolution",
            {}
        )


        if not evolution.get("evolved"):

            return {
                "updated": False,
                "reason": "no evolution"
            }



        for item in self.memory.memory:


            if item.get("id") != project_id:
                continue


            files = item.get(
                "files",
                []
            )


            for file in evolution.get(
                "modules",
                []
            ):

                if file not in files:
                    files.append(file)



            item["files"] = files


            item["evolution_applied"] = True


            item["evolution_features"] = evolution.get(
                "improvements",
                []
            )


            # یادگیری دائمی تجربه
            learn_result = self.experience_memory.learn_from_project(
                item
            )


            self.memory.save()


            return {

                "updated": True,

                "project_id": project_id,

                "files_added": evolution.get(
                    "modules",
                    []
                ),

                "experience_learning": learn_result

            }



        return {
            "updated": False,
            "reason": "project not found"
        }
