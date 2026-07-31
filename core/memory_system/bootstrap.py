from datetime import datetime


class LongTermMemory:

    def __init__(self):
        self.data=[]

    def store(self,item):
        self.data.append({
            "time":str(datetime.now()),
            "item":item
        })
        return {
            "status":"stored",
            "count":len(self.data)
        }

    def recall(self):
        return self.data



class SemanticMemory:

    def __init__(self):
        self.concepts={}

    def add(self,key,value):
        self.concepts[key]=value
        return {
            "status":"concept_added",
            "concept":key
        }



class EpisodicMemory:

    def __init__(self):
        self.events=[]

    def remember(self,event):
        self.events.append(event)
        return {
            "status":"event_saved",
            "events":len(self.events)
        }



class KnowledgeGraph:

    def __init__(self):
        self.nodes=[]

    def connect(self,a,b):
        self.nodes.append({
            "from":a,
            "to":b
        })

        return {
            "status":"connected"
        }



class ExperienceConsolidation:

    def consolidate(self,experience):

        return {
            "status":"consolidated",
            "experience":experience
        }



class MemoryRetrieval:

    def search(self,memory):

        return {
            "status":"retrieved",
            "result":memory
        }



long_term_memory = LongTermMemory()
semantic_memory = SemanticMemory()
episodic_memory = EpisodicMemory()
knowledge_graph = KnowledgeGraph()
experience_consolidation = ExperienceConsolidation()
memory_retrieval = MemoryRetrieval()



print("Memory & Knowledge System Active")

print(
long_term_memory.store(
"Sepehr2 digital human growth"
)
)

print(
semantic_memory.add(
"AI",
"intelligence system"
)
)

print(
episodic_memory.remember(
"environment understanding completed"
)
)

print(
knowledge_graph.connect(
"vision",
"knowledge"
)
)

print(
experience_consolidation.consolidate(
"successful learning"
)
)

print(
memory_retrieval.search(
"AI concept"
)
)

