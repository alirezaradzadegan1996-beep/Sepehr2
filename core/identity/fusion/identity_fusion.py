
class IdentityFusion:


    def calculate(
        self,
        voice=False,
        face=False,
        device=False,
        biometric=False
    ):


        score = 0


        if voice:
            score += 25

        if face:
            score += 25

        if device:
            score += 25

        if biometric:
            score += 25



        if score == 100:

            return {
                "owner": True,
                "confidence": 1.0,
                "score": score,
                "status": "OWNER_CONFIRMED"
            }


        elif score >= 50:

            return {
                "owner": False,
                "confidence": score / 100,
                "score": score,
                "status": "PARTIAL_IDENTITY"
            }


        return {
            "owner": False,
            "confidence": score / 100,
            "score": score,
            "status": "UNKNOWN_USER"
        }



identity_fusion = IdentityFusion()

