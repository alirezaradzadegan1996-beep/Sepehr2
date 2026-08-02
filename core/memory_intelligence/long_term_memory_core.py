

class LongTermMemoryCore:


    def save(self, experience):

        return {

            "experience":
                experience,

            "storage":
                "persistent",

            "status":
                "LONG_TERM_MEMORY_ACTIVE"

        }



long_term_memory_core = LongTermMemoryCore()

