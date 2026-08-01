import importlib


class CapabilityTester:


    def test(self, name):

        result = {

            "capability": name,

            "valid": False,

            "checks": []

        }


        try:

            module = importlib.import_module(
                f"core.capabilities.{name}"
            )


            result["checks"].append(
                "import_success"
            )


            if hasattr(module,"capability"):

                obj = module.capability


                result["checks"].append(
                    "capability_object_found"
                )


                if hasattr(obj,"can_handle"):

                    result["checks"].append(
                        "can_handle_found"
                    )


                if hasattr(obj,"handle"):

                    result["checks"].append(
                        "handle_found"
                    )


                result["valid"] = True



        except Exception as e:

            result["error"] = str(e)



        return result



capability_tester = CapabilityTester()
