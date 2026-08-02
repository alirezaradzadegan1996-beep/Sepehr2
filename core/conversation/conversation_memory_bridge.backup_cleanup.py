from core.memory.experience_memory import experience_memory
from core.memory.experience_normalizer import experience_normalizer


class ConversationMemoryBridge:

    def save(self, experience):

        normalized = experience_normalizer.normalize(experience)

        experience_memory.save(
            normalized
        )

        return {
            "experience": normalized,
            "memory": "saved",
            "status": "stored"
        }


    def recall(self, keyword=None):

        if keyword:
            return experience_memory.search(keyword)

        return experience_memory.recall()


conversation_memory_bridge = ConversationMemoryBridge()
