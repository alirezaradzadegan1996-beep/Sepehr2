

class ShortTermMemoryEngine:


    def store(self, input_data):

        return {

            "input":
                input_data,

            "context":
                "stored",

            "status":
                "SHORT_TERM_MEMORY_ACTIVE"

        }



short_term_memory_engine = ShortTermMemoryEngine()

