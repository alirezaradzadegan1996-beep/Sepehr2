import os
import subprocess


class TestEngine:


    name = "test_engine"


    def run(self, project):

        path = f"projects/{project}"

        main = os.path.join(
            path,
            "main.py"
        )


        if not os.path.exists(main):

            return {
                "status": "failed",
                "error": "main.py not found"
            }


        try:

            result = subprocess.check_output(
                [
                    "python",
                    main
                ],
                stderr=subprocess.STDOUT
            ).decode()


            return {
                "status": "passed",
                "output": result
            }


        except subprocess.CalledProcessError as e:

            return {
                "status": "failed",
                "output": e.output.decode()
            }



test_engine = TestEngine()
