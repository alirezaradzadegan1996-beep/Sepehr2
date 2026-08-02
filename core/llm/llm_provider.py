
class LLMProvider:

    def generate(self, prompt):

        return {
            "prompt": prompt,
            "response": "generated_response",
            "status": "generated"
        }


llm_provider = LLMProvider()
