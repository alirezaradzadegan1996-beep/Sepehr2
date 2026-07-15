import json

from core.project_knowledge import ProjectKnowledge


class KnowledgeOptimizer:

    def __init__(self):

        self.memory = ProjectKnowledge()


    def optimize(
        self,
        analysis
    ):

        project_type = analysis.get(
            "type",
            "general"
        )

        knowledge = self.memory.get_knowledge(
            project_type
        )


        features = analysis.get(
            "features",
            []
        )


        files = analysis.get(
            "files",
            []
        )


        # اضافه کردن الگوهای موفق قبلی

        for item in knowledge.get(
            "successful_patterns",
            []
        ):

            if item not in features:

                features.append(
                    item
                )


        # پیشنهاد فایل بر اساس خطاها و تجربه

        if project_type == "calculator":

            if (
                "ImportError"
                in knowledge.get(
                    "common_errors",
                    []
                )
            ):

                for file in [
                    "errors.py",
                    "validator.py"
                ]:

                    if file not in files:

                        files.append(
                            file
                        )


            if (
                "history"
                in str(features).lower()
            ):

                if "history.py" not in files:

                    files.append(
                        "history.py"
                    )


        analysis["features"] = features

        analysis["files"] = files


        analysis["knowledge"] = {

            "used": True,

            "project_type": project_type,

            "patterns": knowledge.get(
                "successful_patterns",
                []
            ),

            "previous_errors": knowledge.get(
                "common_errors",
                []
            )
        }


        return analysis
