
from core.memory.short_term_memory import short_term_memory
from core.memory.long_term_memory import long_term_memory
from core.memory.memory_retrieval import memory_retrieval


class AdvancedMemoryRuntime:

    def process(self, data):

        short = short_term_memory.store(
            data
        )

        long = long_term_memory.save(
            data
        )

        recall = memory_retrieval.search(
            data
        )

        return {
            "short": short,
            "long": long,
            "recall": recall,
            "status": "MEMORY_ACTIVE"
        }


advanced_memory_runtime = AdvancedMemoryRuntime()
