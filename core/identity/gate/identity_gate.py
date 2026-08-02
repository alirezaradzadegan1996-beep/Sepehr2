
from core.identity.fusion.identity_fusion import identity_fusion


class IdentityGate:


    def check(
        self,
        voice=False,
        face=False,
        device=False,
        biometric=False
    ):


        result = identity_fusion.calculate(
            voice,
            face,
            device,
            biometric
        )


        if result["owner"]:

            return {
                "access": True,
                "route": "runtime",
                "identity": result,
                "status": "OWNER_ACCESS_GRANTED"
            }


        return {
            "access": False,
            "route": "activation",
            "identity": result,
            "status": "ACTIVATION_REQUIRED"
        }



identity_gate = IdentityGate()

