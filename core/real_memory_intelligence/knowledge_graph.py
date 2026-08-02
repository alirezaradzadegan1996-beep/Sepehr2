

class KnowledgeGraph:

    def connect(self,experience):
        return {
            "experience":experience,
            "relations":"created",
            "status":"EXPERIENCE_KNOWLEDGE_GRAPH_ACTIVE"
        }


knowledge_graph=KnowledgeGraph()

