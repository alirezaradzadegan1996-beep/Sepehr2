

class ArchitectureGenerator:

    def generate(self,requirements):
        return {
            "requirements":requirements,
            "architecture":"generated",
            "status":"ARCHITECTURE_GENERATOR_ACTIVE"
        }


architecture_generator=ArchitectureGenerator()

