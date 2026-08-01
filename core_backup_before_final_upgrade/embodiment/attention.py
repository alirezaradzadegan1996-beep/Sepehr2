class AttentionSystem:


    def focus(self, inputs):

        if not inputs:
            return {
                "focus":"none"
            }


        return {
            "focus":inputs[0],
            "priority":"high"
        }


attention_system = AttentionSystem()
