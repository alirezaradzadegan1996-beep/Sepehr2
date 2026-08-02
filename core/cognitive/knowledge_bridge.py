from core.knowledge.knowledge_brain import brain


class KnowledgeBridge:

    def query(self, topic):

        try:
            return brain.query(topic)

        except Exception as e:

            return {
                "topic": topic,
                "answer": None,
                "source": "knowledge_bridge",
                "status": "error",
                "error": str(e)
            }


knowledge_bridge = KnowledgeBridge()
