class ActionSelection:


    def select(self, actions):

        if not actions:
            return {
                "action":"none"
            }


        return {
            "action":actions[0],
            "status":"selected"
        }


action_selection = ActionSelection()
