
class WorldPerception:

    def analyze(self, data):

        return {
            "input": data,
            "objects": [],
            "environment": "known",
            "status": "analyzed"
        }


world_perception = WorldPerception()
