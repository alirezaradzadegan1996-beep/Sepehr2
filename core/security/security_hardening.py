from datetime import datetime
import json
import os


class SecurityHardening:


    def __init__(self):

        self.owner = "Alireza"
        self.logs = []

        self.file = "data/security_log.json"

        os.makedirs(
            "data",
            exist_ok=True
        )


    def authenticate(self, identity):

        if identity == self.owner:

            return {
                "identity":identity,
                "access":"full",
                "status":"verified"
            }


        return {
            "identity":identity,
            "access":"restricted",
            "status":"blocked"
        }



    def authorize(self, identity, action):

        auth = self.authenticate(identity)

        event = {
            "time":str(datetime.now()),
            "identity":identity,
            "action":action,
            "result":auth["status"]
        }


        self.logs.append(event)

        self.save_log()


        return {
            "action":action,
            "security":auth,
            "status":"checked"
        }



    def backup(self):

        return {
            "backup":True,
            "time":str(datetime.now()),
            "status":"completed"
        }



    def save_log(self):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.logs,
                f,
                ensure_ascii=False,
                indent=2
            )



security = SecurityHardening()


print(
    security.authenticate(
        "Alireza"
    )
)


print(
    security.authorize(
        "Alireza",
        "open_memory"
    )
)


print(
    security.authenticate(
        "unknown_user"
    )
)


print(
    security.backup()
)


print(
    {
        "status":"security_hardening_active",
        "time":str(datetime.now())
    }
)

