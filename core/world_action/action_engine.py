

class ActionEngine:


    def execute(self,action):

        return {

            "action":action,
            "execution":"completed",
            "status":"WORLD_ACTION_ACTIVE"

        }



action_engine=ActionEngine()

