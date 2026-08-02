
from core.builder.self_builder_bridge import self_builder_bridge
from core.builder.self_builder_executor import self_builder_executor


class SelfBuilderRuntime:

    def create(self, request):

        plan = self_builder_bridge.analyze_request(
            request
        )

        result = self_builder_executor.build(
            plan
        )

        return {
            "plan": plan,
            "builder": result,
            "status": "completed"
        }


self_builder_runtime = SelfBuilderRuntime()
