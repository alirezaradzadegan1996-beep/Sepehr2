
class ActionSelection:

    def choose(self, decision):

        return {
            "decision": decision,
            "action": "execute",
            "status": "selected"
        }


action_selection_upgrade = ActionSelection()
