

class MemoryRanker:

    def rank(self,memory):
        return {
            "memory":memory,
            "priority":"calculated",
            "status":"MEMORY_RANKING_ACTIVE"
        }


memory_ranker=MemoryRanker()

