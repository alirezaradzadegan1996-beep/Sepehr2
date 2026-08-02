from datetime import datetime


class PersonalCortexGateway:


    def __init__(self):

        self.owner = "Alireza"
        self.memory = []



    def authenticate(self, identity):

        if identity == self.owner:

            return {
                "identity": identity,
                "verified": True,
                "status":"owner_confirmed"
            }


        return {
            "identity": identity,
            "verified": False,
            "status":"guest"
        }



    def process(self, identity, message):

        auth = self.authenticate(identity)


        if not auth["verified"]:

            return {
                "message": message,
                "response":"access denied",
                "status":"blocked"
            }


        result = {
            "message": message,
            "cortex":"activated",
            "decision":"process_request",
            "status":"executed"
        }


        self.memory.append(result)


        return {
            "authentication": auth,
            "result": result,
            "memory_count": len(self.memory)
        }



gateway = PersonalCortexGateway()


print(
    gateway.process(
        "Alireza",
        "سلام سپهر"
    )
)


print(
    gateway.process(
        "unknown_user",
        "سلام"
    )
)


print(
    {
        "status":"personal_cortex_gateway_active",
        "time":str(datetime.now())
    }
)

