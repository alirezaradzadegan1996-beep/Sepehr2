from datetime import datetime


class FinalIntegration:

    def __init__(self):

        self.memory=[]


    def perceive(self):

        return {
            "vision":"object_detected",
            "voice":"speech_detected",
            "status":"perceived"
        }


    def reason(self, perception):

        return {
            "input":perception,
            "analysis":"environment interpreted",
            "status":"reasoned"
        }


    def decide(self, reasoning):

        return {
            "decision":"respond_to_environment",
            "based_on":reasoning,
            "status":"decided"
        }


    def act(self, decision):

        return {
            "action":"generate_response",
            "decision":decision,
            "status":"executed"
        }


    def remember(self, event):

        self.memory.append(event)

        return {
            "saved":True,
            "memory_count":len(self.memory)
        }


    def talk(self, action):

        return {
            "reply":"Environment analysis completed",
            "personality":"Sepehr",
            "status":"ready"
        }



system = FinalIntegration()


perception = system.perceive()
print(perception)

reasoning = system.reason(perception)
print(reasoning)

decision = system.decide(reasoning)
print(decision)

action = system.act(decision)
print(action)

print(
    system.remember(action)
)

print(
    system.talk(action)
)


print(
    {
        "status":"final_integration_complete",
        "time":str(datetime.now())
    }
)

