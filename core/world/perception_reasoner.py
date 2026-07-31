class PerceptionReasoner:


    def analyze(self, observation):


        if not observation:

            return {
                "status":"no_observation"
            }


        objects = observation.get(
            "objects",
            []
        )


        confidence = 0.5


        if objects:

            conclusion = (
                f"detected {len(objects)} object(s)"
            )

        else:

            conclusion = "nothing detected"



        return {

            "status":"interpreted",

            "source":"vision",

            "objects":objects,

            "conclusion":conclusion,

            "confidence":confidence

        }



perception_reasoner = PerceptionReasoner()
