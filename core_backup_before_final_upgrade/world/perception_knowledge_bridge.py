class PerceptionKnowledgeBridge:


    def __init__(self):

        self.memory = []



    def store(self, perception):


        if not perception:

            return {
                "status":"empty"
            }



        fact = {

            "type":"visual_observation",

            "source": perception.get(
                "source"
            ),

            "content": perception.get(
                "conclusion"
            ),

            "objects": perception.get(
                "objects"
            ),

            "confidence": perception.get(
                "confidence"
            )

        }


        self.memory.append(
            fact
        )


        return {

            "status":"stored",

            "fact":fact

        }



    def recall(self):

        return self.memory



perception_knowledge_bridge = PerceptionKnowledgeBridge()
