from datetime import datetime


class SecureExecution:


    def __init__(self):

        self.owner = "Alireza"
        self.memory = []



    def verify_owner(self, identity):

        if identity == self.owner:

            return True

        return False



    def execute(self, identity, action):

        if not self.verify_owner(identity):

            return {
                "action": action,
                "status":"blocked",
                "reason":"unauthorized"
            }


        result = {
            "action": action,
            "status":"executed",
            "security":"verified"
        }


        self.memory.append(
            {
                "time":str(datetime.now()),
                "event":result
            }
        )


        return {
            "execution":result,
            "memory_saved":True,
            "memory_count":len(self.memory)
        }



secure = SecureExecution()


print(
    secure.execute(
        "Alireza",
        "observe_world"
    )
)


print(
    secure.execute(
        "unknown_user",
        "open_memory"
    )
)


print(
    {
        "status":"secure_execution_active",
        "time":str(datetime.now())
    }
)

