
from core.llm.llm_provider import llm_provider


class LLMRouter:

    def route(self, request):

        return llm_provider.generate(
            request
        )


llm_router = LLMRouter()
