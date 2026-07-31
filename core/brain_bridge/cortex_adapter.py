from datetime import datetime


class CortexAdapter:

    def __init__(self):

        self.services = []


    def connect_services(self):

        self.services = [
            "cortex",
            "decision_engine",
            "action_chain",
            "memory",
            "knowledge"
        ]

        return {
            "services": self.services,
            "status": "connected"
        }



    def run(self, text):

        context = {
            "input": text,
            "stage": "context"
        }


        reasoning = {
            "analysis": "reasoning_completed",
            "context": context
        }


        decision = {
            "decision": "execute_action",
            "reasoning": reasoning
        }


        action = {
            "action": "process_request",
            "decision": decision
        }


        return {
            "input": text,
            "context": context,
            "reasoning": reasoning,
            "decision": decision,
            "action": action,
            "status": "completed"
        }



adapter = CortexAdapter()


print(
    adapter.connect_services()
)


print(
    adapter.run(
        "hello sepehr"
    )
)


print(
    {
        "status":"cortex_adapter_active",
        "time":str(datetime.now())
    }
)

