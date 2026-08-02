

class SemanticMemory:


    def convert(self, experience):

        return {

            "input":
                experience,

            "meaning":
                "extracted",

            "memory_type":
                "semantic",

            "status":
                "SEMANTIC_MEMORY_ACTIVE"

        }



semantic_memory = SemanticMemory()

