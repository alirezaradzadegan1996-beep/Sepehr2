from datetime import datetime


class SelfRepair:

    def analyze(self, test_result):

        if test_result.get("status") == "passed":

            return {
                "repair_needed": False,
                "message": "No repair required"
            }

        return {
            "repair_needed": True,
            "target": test_result.get("capability"),
            "error": test_result.get("error","unknown"),
            "time": str(datetime.now())
        }


    def create_plan(self, analysis):

        if not analysis.get("repair_needed"):

            return {
                "status":"skip"
            }

        return {
            "target": analysis["target"],
            "actions":[
                "inspect_module",
                "fix_error",
                "retest"
            ],
            "status":"ready"
        }


self_repair = SelfRepair()
