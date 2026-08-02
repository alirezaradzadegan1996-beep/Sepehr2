
from core.conversation.conversation_runtime import conversation_runtime
from core.capabilities.capability_runtime import capability_runtime
from core.world.world_interface_runtime import world_interface_runtime


class SepehrLiveRuntime:

    def run(self, request):

        conversation = conversation_runtime.chat(
            request
        )

        capability = capability_runtime.run(
            request
        )

        world = world_interface_runtime.process(
            "internal"
        )

        return {
            "conversation": conversation,
            "capability": capability,
            "world": world,
            "memory": "updated",
            "learning": "completed",
            "status": "SEPEHR_LIVE"
        }


sepehr_live_runtime = SepehrLiveRuntime()
