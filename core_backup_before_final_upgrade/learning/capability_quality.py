import os


class CapabilityQuality:


    def check(self, name):


        file = f"core/capabilities/{name}.py"


        if not os.path.exists(file):

            return {
                "capability":name,
                "quality":"failed",
                "reason":"file_missing"
            }


        text = open(
            file,
            encoding="utf-8"
        ).read()


        checks = {

            "has_base": 
            "Capability" in text,

            "has_name":
            "name =" in text,

            "has_handler":
            "handle(" in text,

            "has_can_handle":
            "can_handle(" in text

        }


        return {

            "capability":name,

            "quality":
            "passed"
            if all(checks.values())
            else "failed",

            "checks":checks

        }



capability_quality = CapabilityQuality()
