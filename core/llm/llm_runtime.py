
from core.llm.reasoning_bridge import reasoning_bridge


class LLMRuntime:

    def run(self, input_data):

        return reasoning_bridge.think(
            input_data
        )


llm_runtime = LLMRuntime()
