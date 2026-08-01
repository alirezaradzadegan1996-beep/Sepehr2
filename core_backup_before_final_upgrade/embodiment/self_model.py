class SelfModel:

    def __init__(self):
        self.capabilities = []


    def register(self, capability):
        if capability not in self.capabilities:
            self.capabilities.append(capability)

        return {
            "status":"registered",
            "capabilities":self.capabilities
        }


    def describe(self):
        return {
            "abilities":self.capabilities
        }


self_model = SelfModel()
