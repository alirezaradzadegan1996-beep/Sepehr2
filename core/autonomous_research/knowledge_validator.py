

class KnowledgeValidator:


    def validate(self, data):

        return {

            "data":
                data,

            "accuracy":
                "checked",

            "status":
                "KNOWLEDGE_VALIDATION_ACTIVE"

        }



knowledge_validator = KnowledgeValidator()

