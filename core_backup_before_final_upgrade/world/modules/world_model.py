class WorldModel:

    def __init__(self):
        self.entities = []

    def update(self, data):
        self.entities.append(data)
        return {
            "status":"active",
            "entities":self.entities
        }


world_model = WorldModel()
