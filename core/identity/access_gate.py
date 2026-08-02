from core.identity.owner_profile import owner_profile


class AccessGate:


    def verify_owner(self, name):

        owner = owner_profile.get_owner()


        if owner.get("name") == name:

            return {
                "access": True,
                "level": "OWNER",
                "status": "OWNER_VERIFIED"
            }


        return {
            "access": False,
            "level": "UNKNOWN",
            "status": "OWNER_NOT_VERIFIED"
        }



access_gate = AccessGate()
