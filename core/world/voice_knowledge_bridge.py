class VoiceKnowledgeBridge:


    def __init__(self):

        self.memory = []



    def store(self, perception):


        if not perception:

            return {
                "status":"empty"
            }



        fact = {

            "type":"audio_observation",

            "source": perception.get(
                "source"
            ),

            "content": perception.get(
                "text"
            ),

            "language": perception.get(
                "language"
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



voice_knowledge_bridge = VoiceKnowledgeBridge()
