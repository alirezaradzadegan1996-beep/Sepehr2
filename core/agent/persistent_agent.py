
from core.agent.runtime_loop import runtime_loop
from core.agent.service_manager import service_manager


class PersistentAgent:

    def start(self):

        service = service_manager.start()

        loop = runtime_loop.start(
            cycles=3
        )

        return {
            "service": service,
            "runtime": loop,
            "status": "PERSISTENT_ACTIVE"
        }


persistent_agent = PersistentAgent()
