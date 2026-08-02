

class EpisodicMemory:

    def store(self,experience):
        return {
            "experience":experience,
            "type":"episode",
            "status":"EPISODIC_MEMORY_ACTIVE"
        }


episodic_memory=EpisodicMemory()

