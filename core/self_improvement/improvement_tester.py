class ImprovementTester:

    def test(self, patch):

        results=[]

        for item in patch.get("patches", []):

            risk=item.get("risk")

            if risk in ["low","medium"]:

                results.append({
                    "target":item.get("target"),
                    "status":"approved_for_test",
                    "risk":risk
                })

            else:

                results.append({
                    "target":item.get("target"),
                    "status":"blocked",
                    "risk":risk
                })


        approved = all(
            x["status"]=="approved_for_test"
            for x in results
        )

        return {
            "status":
            "test_ready" if approved else "blocked",

            "results":results
        }


improvement_tester = ImprovementTester()
