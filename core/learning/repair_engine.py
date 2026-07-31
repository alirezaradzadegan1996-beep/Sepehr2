from core.learning.capability_tester import capability_tester


class RepairEngine:


    def repair(self, name):

        test = capability_tester.test(name)


        if test["valid"]:

            return {

                "status": "healthy",

                "capability": name

            }


        error = test.get(
            "error",
            "unknown error"
        )


        return {

            "status": "repair_needed",

            "capability": name,

            "error": error,

            "plan": [

                "analyze error",

                "modify capability",

                "run test again"

            ]

        }



repair_engine = RepairEngine()
