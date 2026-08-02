

class CapabilityGenerator:


    def generate(self, need):

        return {

            "need":
                need,

            "capability":
                "created",

            "status":
                "CAPABILITY_GENERATOR_ACTIVE"

        }



capability_generator = CapabilityGenerator()

