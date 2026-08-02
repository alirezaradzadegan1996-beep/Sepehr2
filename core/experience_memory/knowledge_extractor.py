

class KnowledgeExtractor:


    def extract(self, pattern):

        return {

            "knowledge":
                "generated",

            "source":
                pattern,

            "status":
                "KNOWLEDGE_EXTRACTION_ACTIVE"

        }


knowledge_extractor = KnowledgeExtractor()

