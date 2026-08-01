from datetime import datetime


from core.memory.memory_ranker import memory_ranker
from core.memory.reflection_engine import reflection_engine
from core.memory.forgetting_system import forgetting_system
from core.memory.consolidation_engine import consolidation_engine


class MemoryManager:

    def __init__(self):

        self.memories = {}

        self._load_modules()


    def _load_modules(self):

        try:
            from core.memory.experience_memory import ExperienceMemory
            self.memories["experience"] = ExperienceMemory()
        except Exception:
            self.memories["experience"] = None


        try:
            from core.memory.permanent_memory import PermanentMemory
            self.memories["permanent"] = PermanentMemory()
        except Exception:
            self.memories["permanent"] = None


        try:
            from core.memory.strategy_memory import StrategyMemory
            self.memories["strategy"] = StrategyMemory()
        except Exception:
            self.memories["strategy"] = None


        try:
            from core.memory.observation_memory import ObservationMemory
            self.memories["observation"] = ObservationMemory()
        except Exception:
            self.memories["observation"] = None


        try:
            from core.knowledge.knowledge_brain import KnowledgeBrain
            self.memories["knowledge"] = KnowledgeBrain()
        except Exception:
            self.memories["knowledge"] = None



    def save(self, data, memory_type="experience"):

        memory = self.memories.get(memory_type)

        if memory and hasattr(memory, "save"):

            return memory.save(data)


        return {
            "status":"saved",
            "memory":memory_type,
            "time":str(datetime.now())
        }



    def learn_knowledge(self, topic, information):

        knowledge = self.memories.get("knowledge")

        if knowledge and hasattr(knowledge, "learn"):

            result = knowledge.learn(
                topic,
                information
            )

            return {
                "status":"knowledge_saved",
                "result":result
            }

        return {
            "status":"knowledge_unavailable"
        }



    def recall_knowledge(self, topic):

        knowledge = self.memories.get("knowledge")

        if knowledge and hasattr(knowledge, "query"):

            return {
                "status":"knowledge_loaded",
                "result":knowledge.query(topic)
            }

        return {
            "status":"knowledge_unavailable"
        }



    def save_permanent(self, item):

        memory = self.memories.get("permanent")

        if memory and hasattr(memory, "save"):

            result = memory.save(item)

            return {
                "status":"permanent_saved",
                "result":result
            }


        return {
            "status":"permanent_memory_unavailable"
        }



    def recall_permanent(self):

        memory = self.memories.get("permanent")

        if memory and hasattr(memory, "recall"):

            return {
                "status":"permanent_loaded",
                "result":memory.recall()
            }


        return {
            "status":"permanent_memory_unavailable"
        }



    def remember_experience(
        self,
        text,
        capability,
        status="success",
        description=""
    ):

        memory = self.memories.get("experience")

        if memory and hasattr(memory, "remember"):

            result = memory.remember(
                text,
                capability,
                status,
                description
            )

            if hasattr(memory, "save"):
                memory.save()

            return {
                "status":"experience_saved",
                "result":result
            }


        return {
            "status":"experience_memory_unavailable"
        }



    def recall(self, query=None):

        results=[]

        for name, memory in self.memories.items():

            if memory and hasattr(memory,"recall"):

                try:
                    results.append({
                        "memory":name,
                        "data":memory.recall(query)
                    })

                except Exception:
                    pass


        return results



    def search(self, query):

        return self.recall(query)



    def rank(self, items):

        return memory_ranker.rank(items)



    def consolidate(self, memories=None):

        if memories is None:
            memories = []

        return consolidation_engine.consolidate(
            memories
        )



    def reflect(self, experiences=None):

        if experiences is not None:

            return reflection_engine.reflect(
                experiences
            )

        return {
            "status":"reflection_ready",
            "memory_count":len(self.memories)
        }



    def forget(self, memories=None):

        if memories is None:
            memories = []

        return forgetting_system.forget(
            memories
        )



memory_manager = MemoryManager()
