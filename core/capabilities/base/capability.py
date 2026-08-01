class Capability:


    name = "unknown"
    purpose = "general capability"
    keywords = []


    def __init__(self):

        self.active = False
        self.knowledge = []
        self.version = 1




    def can_handle(self, text):
        text = text.lower()

        patterns = []

        patterns.extend(
            getattr(self, "keywords", [])
        )

        patterns.extend(
            getattr(self, "aliases", [])
        )

        name = getattr(self, "name", "")
        if name:
            patterns.append(name)

        for item in patterns:
            try:
                if str(item).lower() in text:
                    return True
            except:
                pass

        return False

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
