
from core.identity.gate.identity_gate import identity_gate


class RuntimeSecurity:


    def authorize(
        self,
        voice=False,
        face=False,
        device=False,
        biometric=False
    ):


        result = identity_gate.check(
            voice,
            face,
            device,
            biometric
        )


        if result["access"]:

            return {
                "allowed": True,
                "status": "SECURITY_APPROVED",
                "identity": result
            }


        return {
            "allowed": False,
            "status": "SECURITY_BLOCKED",
            "action": "ACTIVATION_REQUIRED",
            "identity": result
        }



runtime_security = RuntimeSecurity()

