from datetime import datetime


class SelfModel:


    def __init__(self):

        self.identity = {
            "name":"Sepehr",
            "type":"digital_agent",
            "owner":"Alireza"
        }

        self.capabilities = []

        self.experiences = []



    def register_capability(self, capability):

        self.capabilities.append(capability)

        return {
            "capability": capability,
            "status":"registered"
        }



    def learn_experience(self, experience):

        self.experiences.append(experience)

        return {
            "experience": experience,
            "status":"learned"
        }



    def self_check(self):

        return {
            "identity": self.identity,
            "capabilities": self.capabilities,
            "experiences": len(self.experiences),
            "self_awareness":"active",
            "status":"understood"
        }



sepehr_self = SelfModel()


print(
    sepehr_self.register_capability(
        "voice"
    )
)


print(
    sepehr_self.register_capability(
        "vision"
    )
)


print(
    sepehr_self.learn_experience(
        "completed owner integration"
    )
)


print(
    sepehr_self.self_check()
)


print(
    {
        "status":"self_model_awareness_active",
        "time":str(datetime.now())
    }
)

