

class ExperienceKnowledgeConverter:


    def convert(self, experience):

        return {

            "experience":
                experience,

            "pattern":
                "identified",

            "knowledge":
                "generated",

            "status":
                "EXPERIENCE_KNOWLEDGE_CONVERSION_ACTIVE"

        }



experience_knowledge_converter = ExperienceKnowledgeConverter()

