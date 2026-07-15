import os
import subprocess


class TestEngine:

    def run(self, project):

        if not project:
            return {
                "success": False,
                "error": "empty project"
            }

        project_id = project.get("id")

        if not project_id:
            return {
                "success": False,
                "error": "missing project id"
            }

        project_dir = os.path.join(
            "projects",
            project_id
        )

        if not os.path.exists(project_dir):
            return {
                "success": False,
                "error": "project folder not found",
                "path": project_dir
            }


        analysis = project.get(
            "analysis",
            {}
        )

        project_type = analysis.get(
            "type",
            "general"
        )


        files = []

        for file in os.listdir(project_dir):
            if file.endswith(".py"):
                files.append(file)



        result = {
            "success": False,
            "project_id": project_id,
            "type": project_type,
            "files": files,
            "error": None,
            "traceback": None,
            "output": None
        }


        test_file = os.path.join(
            project_dir,
            "test.py"
        )


        if not os.path.exists(test_file):

            result["error"] = "test.py missing"
            return result



        try:

            output = subprocess.run(
                [
                    "python",
                    "test.py"
                ],
                cwd=project_dir,
                capture_output=True,
                text=True,
                timeout=10
            )


            if output.returncode == 0:

                result["success"] = True
                result["output"] = output.stdout

            else:

                result["error"] = "test failed"
                result["traceback"] = output.stderr


        except Exception as e:

            result["error"] = str(e)



        return result
