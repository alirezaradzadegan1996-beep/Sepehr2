

class CapabilityBuilder:


    def build(self, upgrade):

        return {

            "capability":
                "created",

            "deployment":
                "completed",

            "status":
                "CAPABILITY_BUILDER_ACTIVE"

        }


capability_builder = CapabilityBuilder()

