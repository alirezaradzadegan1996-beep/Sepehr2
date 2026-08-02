

class EpisodicMemory:


    def store(self, experience):

        return {

            "experience": experience,

            "memory_type":
                "episodic",

            "status":
                "EPISODIC_MEMORY_ACTIVE"

        }



episodic_memory = EpisodicMemory()

