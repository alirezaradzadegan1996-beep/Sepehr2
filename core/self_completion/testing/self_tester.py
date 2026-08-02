class SelfTester:

    def test(self, capability):

        result = {
            "capability": capability,
            "status": "unknown"
        }

        try:
            obj = __import__(
                f"core.capabilities.{capability}",
                fromlist=["capability"]
            )

            if hasattr(obj, "capability"):

                result["status"] = "passed"
                result["message"] = "Capability loaded successfully"

            else:
                result["status"] = "failed"
                result["message"] = "Capability object missing"

        except Exception as e:

            result["status"] = "failed"
            result["error"] = str(e)

        return result


self_tester = SelfTester()
