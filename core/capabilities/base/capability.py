class Capability:


    name = "unknown"


    def __init__(self):

        self.active = False
        self.knowledge = []
        self.version = 1



    def activate(self):

        self.active = True

        return {
            "capability": self.name,
            "status":"active"
        }



    def learn(self, data):

        self.knowledge.append(data)

        return {
            "capability": self.name,
            "learned": data
        }



    def improve(self):

        self.version += 1

        return {
            "capability": self.name,
            "version": self.version
        }
