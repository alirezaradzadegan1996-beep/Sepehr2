from datetime import datetime


class AccessControl:


    def __init__(self):

        self.owner = "Alireza"



    def check(self, identity):

        if identity == self.owner:

            return {
                "identity": identity,
                "access": "full",
                "cortex": "unlocked",
                "status": "authorized"
            }


        return {
            "identity": identity,
            "access": "guest",
            "cortex": "locked",
            "status": "restricted"
        }



    def protect_action(self, identity, action):

        result = self.check(identity)


        if result["status"] == "authorized":

            return {
                "action": action,
                "execution": "allowed",
                "security": result
            }


        return {
            "action": action,
            "execution": "blocked",
            "security": result
        }



security = AccessControl()


print(
    security.check(
        "Alireza"
    )
)


print(
    security.protect_action(
        "Alireza",
        "open_memory"
    )
)


print(
    security.check(
        "unknown_user"
    )
)


print(
    {
        "status":"access_control_active",
        "time":str(datetime.now())
    }
)

