
class CapabilityGenome:

    def __init__(self):
        self.registry = {}


    def register(self, name, version):

        self.registry[name] = {
            "version": version,
            "status": "registered"
        }

        return {
            "capability": name,
            "version": version,
            "registry": self.registry,
            "status": "CAPABILITY_GENOME_ACTIVE"
        }


capability_genome = CapabilityGenome()
